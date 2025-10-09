/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.editor.model.compatibility;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

import java.io.File;
import java.io.IOException;

import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.Resource.Diagnostic;
import org.junit.jupiter.api.Test;

import com.archimatetool.editor.TestSupport;
import com.archimatetool.model.IArchimateModel;
import com.archimatetool.model.util.ArchimateResourceFactory;


@SuppressWarnings("nls")
public class ModelCompatibilityTests {
    
    private ModelCompatibility mc;
    private Resource resource;
    
    File file1 = new File(TestSupport.getTestDataFolder(), "models/compatibility_test1.archimate");
    File file2 = new File(TestSupport.getTestDataFolder(), "models/compatibility_test2.archimate");
    
    @Test
    public void testShouldThrowException1() {
        resource = ArchimateResourceFactory.createNewResource(file1);
        assertThrows(IOException.class, () -> {
            resource.load(null);
        });
    }

    @Test
    public void testShouldThrowException2() {
        resource = ArchimateResourceFactory.createNewResource(file2);
        assertThrows(IOException.class, () -> {
            resource.load(null);
        });
    }

    @Test
    public void testCheckErrors_ThrowsException() {
        createResource(file2);
        assertThrows(IncompatibleModelException.class, () -> {
            mc.checkErrors();
        });
    }
    
    @Test
    public void testCheckErrors_NotCatastrophic() throws IncompatibleModelException {
        createResource(file1);
        mc.checkErrors();
    }

    @Test
    public void testCheckErrors_IsCatastrophic() {
        createResource(file2);
        try {
            mc.checkErrors();
        }
        catch(IncompatibleModelException ex) {
            return;
        }
        
        fail();
    }

    @Test
    public void testIsLaterModelVersion_IsLater() {
        createResource(file1);
        IArchimateModel model = (IArchimateModel)resource.getContents().get(0);
        assertEquals("10.0.0", model.getVersion());
        assertTrue(mc.isLaterModelVersion("2.6.1"));
    }

    @Test
    public void testIsLaterModelVersion_IsNotLater() {
        createResource(file1);
        IArchimateModel model = (IArchimateModel)resource.getContents().get(0);
        
        model.setVersion("3.4.1");
        assertFalse(mc.isLaterModelVersion("10.0.0"));
        
        model.setVersion("99.9.9");
        assertFalse(mc.isLaterModelVersion("99.9.9"));
    }

    @Test
    public void testgetAcceptableExceptions() {
        createResource(file1);
        assertEquals(2,  mc.getAcceptableExceptions().size());
        
        createResource(file2);
        assertEquals(0,  mc.getAcceptableExceptions().size());
    }

    @Test
    public void testIsFeatureNotFoundException() {
        createResource(file1);
        
        assertEquals(2,  resource.getErrors().size());
        
        Diagnostic diagnostic = resource.getErrors().get(0);
        assertTrue(mc.isFeatureNotFoundException(diagnostic));
        
        diagnostic = resource.getErrors().get(1);
        assertTrue(mc.isFeatureNotFoundException(diagnostic));
    }

    @Test
    public void testIsCatastrophicException() {
        createResource(file2);
        
        assertEquals(2,  resource.getErrors().size());
        
        Diagnostic diagnostic = resource.getErrors().get(0);
        assertTrue(mc.isCatastrophicException(diagnostic));
        
        diagnostic = resource.getErrors().get(1);
        assertTrue(mc.isCatastrophicException(diagnostic));
    }
    
    private void createResource(File file) {
        resource = ArchimateResourceFactory.createNewResource(file);
        mc = new ModelCompatibility(resource);
        mc.doLog = false;
        
        try {
            resource.load(null);
        }
        catch(IOException ex) {
            // Should happen
        }
    }
}
