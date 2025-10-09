/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.model.util;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.File;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.junit.jupiter.api.Test;

import com.archimatetool.model.TestSupport;



/**
 * ArchimateModelUtils Tests
 *
 * @author Phillip Beauvoir
 */
@SuppressWarnings("nls")
public class ArchimateResourceFactoryTests {

    @Test
    public void testCreateNewResource_File() {
        File file = TestSupport.TEST_MODEL_FILE_ARCHISURANCE;
        Resource resource = ArchimateResourceFactory.createNewResource(file);
        
        assertEquals(file, new File(resource.getURI().toFileString()));
        assertFalse(resource.isLoaded());
        assertNotNull(resource.getResourceSet());
        assertTrue(resource.getContents().isEmpty());
    }
 
    @Test
    public void testCreateNewResource_URI() {
        URI uri = URI.createFileURI(TestSupport.TEST_MODEL_FILE_ARCHISURANCE.getPath());
        Resource resource = ArchimateResourceFactory.createNewResource(uri);
        
        assertEquals(uri, resource.getURI());
        assertFalse(resource.isLoaded());
        assertNotNull(resource.getResourceSet());
        assertTrue(resource.getContents().isEmpty());
    }

    @Test
    public void testCreateResourceSet() {
        ResourceSet resourceSet = ArchimateResourceFactory.createResourceSet();
        
        assertTrue(resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap().get("*") instanceof ArchimateResourceFactory);
        assertTrue(resourceSet.getResources().isEmpty());
    }

    @Test
    public void testCreateResource() {
        ArchimateResourceFactory factory = new ArchimateResourceFactory();
        
        URI uri = URI.createFileURI(TestSupport.TEST_MODEL_FILE_ARCHISURANCE.getPath());
        
        Resource resource = factory.createResource(uri);
        
        assertEquals(uri, resource.getURI());
        assertFalse(resource.isLoaded());
        assertNull(resource.getResourceSet());
        assertTrue(resource.getContents().isEmpty());
    }
} 
