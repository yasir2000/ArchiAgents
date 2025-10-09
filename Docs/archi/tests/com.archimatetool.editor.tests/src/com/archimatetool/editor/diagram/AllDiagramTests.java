/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.editor.diagram;

import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;
import org.junit.platform.suite.api.SuiteDisplayName;

import com.archimatetool.editor.diagram.actions.CopySnapshotTests;
import com.archimatetool.editor.diagram.actions.SelectAllActionTests;
import com.archimatetool.editor.diagram.commands.AllCommandsTests;
import com.archimatetool.editor.diagram.editparts.AllEditPartsTests;
import com.archimatetool.editor.diagram.figures.AllFiguresTests;
import com.archimatetool.editor.diagram.policies.AllPoliciesTests;
import com.archimatetool.editor.diagram.sketch.AllSketchTests;
import com.archimatetool.editor.diagram.tools.FormatPainterInfoTests;
import com.archimatetool.editor.diagram.tools.FormatPainterToolTests;
import com.archimatetool.editor.diagram.util.DiagramUtilsTests;

@Suite
@SelectClasses({
    // diagram
    ArchimateDiagramModelFactoryTests.class,
    DiagramEditorFindReplaceProviderTests.class,
    ImageExportProviderTests.class,
    ImageExportProviderManagerTests.class,
    // diagram.actions
    CopySnapshotTests.class,
    SelectAllActionTests.class,
    // diagram.commands
    AllCommandsTests.class,
    // diagram.editparts
    AllEditPartsTests.class,
    // diagram.figures
    AllFiguresTests.class,
    // diagram.policies
    AllPoliciesTests.class,
    // diagram.sketch
    AllSketchTests.class,
    // diagram.tools
    FormatPainterInfoTests.class,
    FormatPainterToolTests.class,
    // diagram.util
    DiagramUtilsTests.class
})
@SuiteDisplayName("All Diagram Tests")
public class AllDiagramTests {
}