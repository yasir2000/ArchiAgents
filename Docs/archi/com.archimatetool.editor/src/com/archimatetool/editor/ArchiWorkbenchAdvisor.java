/**
 * This program and the accompanying materials
 * are made available under the terms of the License
 * which accompanies this distribution in the file LICENSE.txt
 */
package com.archimatetool.editor;

import org.eclipse.jface.dialogs.TrayDialog;
import org.eclipse.jface.preference.IPreferenceNode;
import org.eclipse.jface.preference.PreferenceManager;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.IWorkbenchPreferenceConstants;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.application.IWorkbenchConfigurer;
import org.eclipse.ui.application.IWorkbenchWindowConfigurer;
import org.eclipse.ui.application.WorkbenchAdvisor;
import org.eclipse.ui.application.WorkbenchWindowAdvisor;

import com.archimatetool.editor.perspectives.MainPerspective;
import com.archimatetool.editor.preferences.IPreferenceConstants;
import com.archimatetool.editor.utils.NetUtils;
import com.archimatetool.editor.utils.PlatformUtils;


/**
 * The workbench advisor for standalone RCP.
 * Configures the workbench as needed, including specifying the default perspective id.
 * Configures each new workbench window as it is being opened.
 * 
 * @author Phillip Beauvoir
 */
@SuppressWarnings("nls")
public class ArchiWorkbenchAdvisor
extends WorkbenchAdvisor
{
	/**
	 * Constructor
	 */
	public ArchiWorkbenchAdvisor() {
	}
	
    @Override
    public void initialize(IWorkbenchConfigurer configurer) {
        super.initialize(configurer);
        
        // Save and restore stuff
        configurer.setSaveAndRestore(true);
        
        // If System Property in VM arguments is "-Dshowheap=true" then Show Heap Widget
        PlatformUI.getPreferenceStore().setValue(IWorkbenchPreferenceConstants.SHOW_MEMORY_MONITOR,
                "true".equals(System.getProperty("showheap")));
        
        // Edge Browser on Windows
        if(PlatformUtils.isWindows() && ArchiPlugin.PREFERENCES.getBoolean(IPreferenceConstants.EDGE_BROWSER)) {
            System.setProperty("org.eclipse.swt.browser.DefaultType", "edge");
        }
        
        // Show Help Button by default on Dialogs
        TrayDialog.setDialogHelpAvailable(true);
        
        // Move some preference pages to new parents
        PreferenceManager pm = PlatformUI.getWorkbench().getPreferenceManager();
        if(pm != null) {
            IPreferenceNode systemNode = pm.find("org.eclipse.ui.preferencePages.Workbench");
            if(systemNode != null) {
                // Move "Help" preference page to our "System" page
                IPreferenceNode helpNode = pm.find("org.eclipse.help.ui.browsersPreferencePage");
                if(helpNode != null) {
                    pm.remove(helpNode);
                    systemNode.add(helpNode);
                }
                
                // Move the "Secure Storage" preference page from its container node to our "System" page
                IPreferenceNode securityCategoryNode = systemNode.findSubNode("org.eclipse.equinox.security.ui.category");
                if(securityCategoryNode != null) {
                    IPreferenceNode securityNode = securityCategoryNode.findSubNode("org.eclipse.equinox.security.ui.storage");
                    if(securityNode != null) {
                        // Remove the category node
                        systemNode.remove(securityCategoryNode);
                        // Add security node to our system node
                        systemNode.add(securityNode);
                    }
                }
            }
        }
        
        // Initialise Proxy
        NetUtils.initialise();
    }
    
    @Override
    public WorkbenchWindowAdvisor createWorkbenchWindowAdvisor(IWorkbenchWindowConfigurer configurer) {
        return new ArchiWorkbenchWindowAdvisor(configurer);
    }

	@Override
    public String getInitialWindowPerspectiveId() {
	    // If null then we could use WorkbenchWindowAdvisor.createEmptyWindowContents(Composite parent)
	    //return null; 
		return MainPerspective.ID;
	}
	
    @Override
    public void eventLoopIdle(Display display) {
        // See if the user has opened files from the Desktop
        // See http://help.eclipse.org/kepler/index.jsp?topic=%2Forg.eclipse.platform.doc.isv%2Fguide%2Fproduct_open_file.htm
        OpenDocumentHandler.getInstance().openQueuedFiles();
        super.eventLoopIdle(display);
    }
    
}
