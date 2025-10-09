/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.model.impl;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.File;

import org.eclipse.emf.common.util.EList;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.archimatetool.model.IArchimateFactory;
import com.archimatetool.model.IArchimateModel;
import com.archimatetool.model.IMetadata;
import com.archimatetool.model.IProperty;
import com.archimatetool.model.TestSupport;



@SuppressWarnings("nls")
public class MetadataTests {
    
    IArchimateModel model;
    IMetadata metadata;
    
    // ---------------------------------------------------------------------------------------------
    // BEFORE AND AFTER METHODS GO HERE 
    // ---------------------------------------------------------------------------------------------
    
    @SuppressWarnings("deprecation")
    @BeforeEach
    public void runBeforeEachTest() {
        model = IArchimateFactory.eINSTANCE.createArchimateModel();
        metadata = IArchimateFactory.eINSTANCE.createMetadata();
        model.setMetadata(metadata);
    }
    
    // ---------------------------------------------------------------------------------------------
    // Tests
    // ---------------------------------------------------------------------------------------------
    
    @Test
    public void testGetEntries() {
        assertNotNull(metadata.getEntries());
        assertEquals(0, metadata.getEntries().size());
    }
    
    @Test
    public void testEntryCreated() throws Exception {
        String key = "some_key", value = "some_value";
        
        // Add a metadata entry as a property key/value pair
        IProperty property = IArchimateFactory.eINSTANCE.createProperty();
        property.setKey(key);
        property.setValue(value);
        metadata.getEntries().add(property);

        // Check entry is correct
        EList<IProperty> entries = metadata.getEntries();
        assertEquals(1, entries.size());
        IProperty testProperty = entries.get(0);
        assertEquals(property, testProperty);
        assertEquals(testProperty.getKey(), key);
        assertEquals(testProperty.getValue(), value);
                
        // Save to file
        File file = TestSupport.saveModel(model);
        assertTrue(file.exists());
        
        // Load it in again
        IArchimateModel testModel = TestSupport.loadModel(file);
        
        // Check it persisted
        @SuppressWarnings("deprecation")
        EList<IProperty> testEntries = testModel.getMetadata().getEntries();
        assertEquals(1, testEntries.size());
        testProperty = testEntries.get(0);
        assertEquals(testProperty.getKey(), key);
        assertEquals(testProperty.getValue(), value);
    }
    
    @Test
    public void testAddEntry() {
        String key = "some_key", value = "some_value";

        IProperty property = metadata.addEntry(key, value);
        assertNotNull(property);
        assertEquals(key, property.getKey());
        assertEquals(value, property.getValue());
        
        // Check entry is correct
        EList<IProperty> entries = metadata.getEntries();
        assertEquals(1, entries.size());
        assertEquals(property, entries.get(0));
    }
    
    @Test
    public void testAddEntryNullException() {
        assertThrows(IllegalArgumentException.class, () -> {
            metadata.addEntry(null, "");
        });
    }
        
    @Test
    public void testGetEntry() {
        String key = "some_key", value = "some_value";
        
        assertNull(metadata.getEntry("something"));
        
        IProperty property = metadata.addEntry(key, value);
        assertEquals(property, metadata.getEntry(key));
    }
    
    @Test
    public void testgetEntryNullException() {
        assertThrows(IllegalArgumentException.class, () -> {
            metadata.getEntry(null);
        });
    }

    @Test
    public void testAddEntryExists() {
        String key ="some_key", value = "some_value", new_value="another_value";

        IProperty property = metadata.addEntry(key, value);
        IProperty property2 = metadata.addEntry(key, new_value);
        
        assertEquals(property, property2);
        assertEquals(new_value, property2.getValue());
    }

}
