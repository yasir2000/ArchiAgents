/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.model.impl;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import com.archimatetool.model.IArchimateDiagramModel;
import com.archimatetool.model.IArchimateFactory;
import com.archimatetool.model.IArchimatePackage;
import com.archimatetool.model.IDiagramModel;


@SuppressWarnings("nls")
public class ArchimateDiagramModelTests extends DiagramModelTests {
    
    private IArchimateDiagramModel adm;
    
    @Override
    protected IDiagramModel getDiagramModel() {
        adm = IArchimateFactory.eINSTANCE.createArchimateDiagramModel();
        return adm;
    }
    
    
    @Test
    public void testGetViewpoint() {
        assertEquals("", adm.getViewpoint());
        adm.setViewpoint("vp_id");
        assertEquals("vp_id", adm.getViewpoint());
    }

    @Test
    public void testGetChildren() {
        CommonTests.testList(adm.getChildren(), IArchimatePackage.eINSTANCE.getDiagramModelArchimateObject());
        CommonTests.testList(adm.getChildren(), IArchimatePackage.eINSTANCE.getDiagramModelGroup());
        CommonTests.testList(adm.getChildren(), IArchimatePackage.eINSTANCE.getDiagramModelNote());
    }

}
