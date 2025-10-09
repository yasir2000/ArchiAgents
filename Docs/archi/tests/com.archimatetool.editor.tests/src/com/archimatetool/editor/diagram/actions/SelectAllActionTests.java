/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.editor.diagram.actions;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Set;

import org.eclipse.gef.GraphicalEditPart;
import org.junit.jupiter.api.Test;

import com.archimatetool.model.IArchimateDiagramModel;
import com.archimatetool.model.IArchimateModel;
import com.archimatetool.model.util.ArchimateModelUtils;
import com.archimatetool.testingtools.ArchimateTestEditor;
import com.archimatetool.testingtools.ArchimateTestModel;
import com.archimatetool.tests.TestData;

/**
 * SelectAllAction Tests
 * 
 * @author Phillip Beauvoir
 */
@SuppressWarnings("nls")
public class SelectAllActionTests {
    
    @Test
    public void testSelectAll() throws Exception {
        ArchimateTestEditor editor = new ArchimateTestEditor();
        
        ArchimateTestModel tm = new ArchimateTestModel(TestData.TEST_MODEL_FILE_ARCHISURANCE);
        IArchimateModel model = tm.loadModelWithCommandStack();
        IArchimateDiagramModel dm = (IArchimateDiagramModel)ArchimateModelUtils.getObjectByID(model, "4165");
        editor.setDiagramModel(dm);
        
        SelectAllAction action = new SelectAllAction(null);
        Set<GraphicalEditPart> selected = action.getSelectableEditParts(editor.getGraphicalViewer().getContents());
        assertEquals(47, selected.size());
        
        editor.dispose();
    }
    
}