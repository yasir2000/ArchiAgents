/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.editor.ui.textrender;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.archimatetool.model.IArchimateDiagramModel;
import com.archimatetool.model.IArchimateFactory;
import com.archimatetool.model.IConnectable;
import com.archimatetool.model.IDiagramModelArchimateConnection;
import com.archimatetool.model.IDiagramModelArchimateObject;
import com.archimatetool.model.IDiagramModelReference;



/**
 * TypeRenderer Tests
 * 
 * @author Phillip Beauvoir
 */
@SuppressWarnings("nls")
public class TypeRendererTests extends AbstractTextRendererTests {

    private TypeRenderer renderer = new TypeRenderer();
    
    private IDiagramModelArchimateObject dmo;
    private IDiagramModelArchimateConnection dmc;
    
    @BeforeEach
    public void beforeEachTest() {
        dmo = TextRendererTests.createDiagramModelObject();
        dmc = TextRendererTests.createDiagramModelConnection();
    }
    
    @Override
    protected TypeRenderer getRenderer() {
        return renderer;
    }
    
    @Test
    public void render_Type_Object() {
        String result = renderer.render(dmo, "${type}");
        assertEquals("Business Actor", result);
    }
    
    @Test
    public void render_Type_Relation() {
        String result = renderer.render(dmc, "${type}");
        assertEquals("Assignment relation", result);
    }
    
    @Test
    public void render_Type_Note() {
        String result = renderer.render(IArchimateFactory.eINSTANCE.createDiagramModelNote(), "${type}");
        assertEquals("Note", result);
    }

    @Test
    public void render_Type_Group() {
        String result = renderer.render(IArchimateFactory.eINSTANCE.createDiagramModelGroup(), "${type}");
        assertEquals("Group", result);
    }
    
    @Test
    public void render_Type_Connection() {
        String result = renderer.render(IArchimateFactory.eINSTANCE.createDiagramModelConnection(), "${type}");
        assertEquals("Connection", result);
    }

    @Test
    public void render_Type_Reference() {
        IArchimateDiagramModel dm = IArchimateFactory.eINSTANCE.createArchimateDiagramModel();
        IDiagramModelReference ref = IArchimateFactory.eINSTANCE.createDiagramModelReference();
        ref.setReferencedModel(dm);
        String result = renderer.render(ref, "${type}");
        assertEquals("View", result);
    }
    
    @Test
    public void render_SourceType() {
        String result = renderer.render(dmc, "$source{type}");
        assertEquals("Business Actor", result);
    }
    
    @Test
    public void render_TargetType() {
        String result = renderer.render(dmc, "$target{type}");
        assertEquals("Business Role", result);
    }

    @Test
    public void render_ParentType() {
        String result = renderer.render(dmo, "$parent{type}");
        assertEquals("View", result);
    }

    @Test
    public void render_ConnectedSourceType() {
        String result = renderer.render(dmc.getTarget(), "$assignment:source{type}");
        assertEquals("Business Actor", result);
    }
    
    @Test
    public void render_ConnectedSourceType_No_DiagramModelComponent() {
        IConnectable target = dmc.getTarget();
        
        // remove dmc
        dmc.disconnect();
        
        String result = renderer.render(target, "$assignment:source{type}");
        assertEquals("Business Actor", result);
    }
    
    @Test
    public void render_ConnectedTargetType() {
        String result = renderer.render(dmc.getSource(), "$assignment:target{type}");
        assertEquals("Business Role", result);
    }

    @Test
    public void render_ConnectedTargetType_No_DiagramModelComponent() {
        IConnectable source = dmc.getSource();
        
        // remove dmc
        dmc.disconnect();
        
        String result = renderer.render(source, "$assignment:target{type}");
        assertEquals("Business Role", result);
    }
    
    @Test
    public void render_ModelFolderName() {
        String result = renderer.render(dmo, "$mfolder{type}");
        assertEquals("Folder", result);
    }
    
    @Test
    public void render_ViewFolderName() {
        String result = renderer.render(dmo, "$vfolder{type}");
        assertEquals("Folder", result);
    }

}
