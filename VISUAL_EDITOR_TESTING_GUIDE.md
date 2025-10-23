# Visual Editor - Testing Guide

## 🧪 Complete Test Plan

Follow this guide to test all Visual Editor features systematically.

---

## Prerequisites

### 1. Start Backend
```bash
cd web_app/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
python main.py
```

✅ Backend should be running at: http://localhost:8000

### 2. Start Frontend
```bash
cd web_app/frontend
npm install  # If not already done
npm run dev
```

✅ Frontend should be running at: http://localhost:3000

---

## Test Suite 1: Application Startup ✅

### Test 1.1: Frontend Compilation
- [ ] Frontend starts without errors
- [ ] No TypeScript compilation errors in terminal
- [ ] Browser console shows no errors
- [ ] Application loads successfully

**Expected:** Clean startup with no errors

### Test 1.2: Navigation
- [ ] Open http://localhost:3000
- [ ] Login page appears
- [ ] Can register new account or login
- [ ] Dashboard loads after login
- [ ] Can navigate to Models page

**Expected:** Smooth navigation through all pages

---

## Test Suite 2: Model Management 📊

### Test 2.1: Create New Model
1. Navigate to Models page
2. Click "Create Model" button
3. Fill in model details:
   - Name: "Test ArchiMate Model"
   - Type: Select "ArchiMate"
   - Description: "Testing visual editor"
4. Click Create

**Expected:**
- [ ] Model created successfully
- [ ] Toast notification appears
- [ ] Model appears in list

### Test 2.2: Open Model in Editor
1. Find the test model in the list
2. Click "Edit" button or model row
3. Editor page loads

**Expected:**
- [ ] ModelEditorPage loads
- [ ] Header shows model name
- [ ] Canvas is visible
- [ ] Element palette on left
- [ ] Properties panel on right (initially empty)
- [ ] Toolbar at top

---

## Test Suite 3: Element Palette 🎨

### Test 3.1: Palette Display
**Check:**
- [ ] Palette is visible on left side
- [ ] "Elements" header shown
- [ ] Search box is present
- [ ] Category tabs visible (all, strategy, business, application, technology)
- [ ] Elements displayed in grid

### Test 3.2: Search Functionality
1. Type "business" in search box
2. Observe filtered results
3. Clear search
4. Type "actor"

**Expected:**
- [ ] Results filter in real-time
- [ ] Only matching elements shown
- [ ] Clear search shows all elements

### Test 3.3: Category Filtering
1. Click "strategy" tab
2. Check elements shown
3. Click "business" tab
4. Click "all" tab

**Expected:**
- [ ] Only strategy elements show
- [ ] Only business elements show
- [ ] All elements show
- [ ] Active tab highlighted

### Test 3.4: Element Information
**Check each element shows:**
- [ ] Icon (colored appropriately)
- [ ] Name
- [ ] Type label
- [ ] Hover effect works

---

## Test Suite 4: Diagram Canvas 🖼️

### Test 4.1: Add Elements from Palette
1. Click "Business Actor" in palette
2. Element should appear on canvas
3. Click "Business Process"
4. Click "Application Component"

**Expected:**
- [ ] Elements appear on canvas
- [ ] Each element has proper shape
- [ ] Colors match element type
- [ ] Labels are visible
- [ ] Elements are selectable

### Test 4.2: Move Elements
1. Click and drag an element
2. Move it to different position
3. Release mouse

**Expected:**
- [ ] Element moves smoothly
- [ ] Cursor changes to move cursor
- [ ] Element stays where released

### Test 4.3: Resize Elements
1. Select an element
2. Look for resize handles (corners)
3. Drag a corner handle
4. Resize element

**Expected:**
- [ ] Resize handles appear when selected
- [ ] Element resizes proportionally
- [ ] Text adjusts within element

### Test 4.4: Select Elements
1. Click an element to select
2. Click another element
3. Click empty canvas to deselect
4. Ctrl+Click multiple elements

**Expected:**
- [ ] Selected element has blue border
- [ ] Only one selected at a time (without Ctrl)
- [ ] Clicking canvas deselects
- [ ] Multi-select works with Ctrl

### Test 4.5: Create Links
1. Click and drag from one element
2. Drop on another element
3. Link should be created

**Expected:**
- [ ] Link appears between elements
- [ ] Arrow points to target
- [ ] Link routes around other elements
- [ ] Can select link by clicking

### Test 4.6: Edit Link Labels
1. Double-click a link
2. Type "uses" or any text
3. Press Enter or click away

**Expected:**
- [ ] Text editor appears on link
- [ ] Can type label
- [ ] Label appears on link

---

## Test Suite 5: Properties Panel 📝

### Test 5.1: Panel Display
1. Select an element on canvas
2. Check properties panel on right

**Expected:**
- [ ] Properties panel shows selected element
- [ ] Element name displayed at top
- [ ] Type shown
- [ ] Property fields visible

### Test 5.2: Edit Name
1. Select an element
2. In properties panel, change Name field
3. Type "Customer" or any name
4. Check canvas

**Expected:**
- [ ] Name field is editable
- [ ] Text updates in real-time on canvas
- [ ] Changes persist

### Test 5.3: Edit Description
1. Select an element
2. Edit Description textarea
3. Type multi-line text

**Expected:**
- [ ] Textarea accepts input
- [ ] Can enter multiple lines
- [ ] Scrolls if needed

### Test 5.4: Change Colors
1. Select an element
2. Click Fill Color color picker
3. Choose a different color
4. Click Border Color color picker
5. Choose a different color

**Expected:**
- [ ] Color picker opens
- [ ] Element color updates immediately
- [ ] Both fill and border change independently
- [ ] Color hex code shows in text field

### Test 5.5: Close Properties Panel
1. Click X button on properties panel
2. Check if panel hides
3. Click "Show Properties" in status bar
4. Panel reappears

**Expected:**
- [ ] Panel hides when X clicked
- [ ] Canvas expands to fill space
- [ ] Panel shows again when toggled

---

## Test Suite 6: Toolbar Actions ⚙️

### Test 6.1: Save Operation
1. Make changes to diagram
2. Click Save button (or Ctrl+S)
3. Check for notification

**Expected:**
- [ ] "Saving..." indicator appears
- [ ] Toast notification: "Model saved successfully"
- [ ] Changes persist if page refreshed

### Test 6.2: Undo/Redo
1. Add an element
2. Click Undo button (or Ctrl+Z)
3. Element disappears
4. Click Redo button (or Ctrl+Y)
5. Element reappears

**Expected:**
- [ ] Undo removes last action
- [ ] Redo restores undone action
- [ ] Buttons disable when no undo/redo available
- [ ] Multiple undo/redo works

### Test 6.3: Delete Element
1. Select an element
2. Click Delete button (trash icon)
3. Or press Delete key

**Expected:**
- [ ] Element is removed from canvas
- [ ] Can undo deletion
- [ ] Properties panel clears

### Test 6.4: Zoom Controls
1. Click Zoom In button (+)
2. Check zoom level indicator
3. Click Zoom Out button (-)
4. Click Fit to Screen button

**Expected:**
- [ ] Zoom increases/decreases
- [ ] Percentage updates in toolbar
- [ ] Fit to Screen shows all elements
- [ ] Diagram remains centered

### Test 6.5: Grid Toggle
1. Click Grid button
2. Check background
3. Click again

**Expected:**
- [ ] Grid appears/disappears
- [ ] Button state indicates grid on/off
- [ ] Grid helps with alignment

### Test 6.6: Auto Layout
1. Add multiple elements randomly
2. Click Auto Layout button
3. Observe arrangement

**Expected:**
- [ ] Elements rearrange automatically
- [ ] Hierarchical layout applied
- [ ] Links remain connected
- [ ] Can undo layout

---

## Test Suite 7: Model Types 📋

### Test 7.1: ArchiMate Model
1. Create new model with type "ArchiMate"
2. Open in editor
3. Check palette has:
   - Strategy elements (yellow)
   - Business elements (yellow)
   - Application elements (blue)
   - Technology elements (light blue)

**Expected:**
- [ ] All 18 ArchiMate elements available
- [ ] Correct colors for each layer
- [ ] Elements have proper shapes

### Test 7.2: BPMN Model
1. Create new model with type "BPMN"
2. Open in editor
3. Check palette has:
   - Tasks, Sub-processes
   - Gateways (diamond)
   - Start/End events (circles)
   - Pools and Lanes

**Expected:**
- [ ] All 7 BPMN elements available
- [ ] Gateway shows as diamond
- [ ] Events show as circles
- [ ] Can create process flow

### Test 7.3: UML Model
1. Create new model with type "UML"
2. Open in editor
3. Check palette has:
   - Class, Interface, Component, Package
   - Actor, Use Case, State

**Expected:**
- [ ] All 7 UML elements available
- [ ] Class has properties section
- [ ] Proper UML notation used

---

## Test Suite 8: Keyboard Shortcuts ⌨️

Test each shortcut:

- [ ] **Ctrl+S** - Saves model
- [ ] **Ctrl+Z** - Undo
- [ ] **Ctrl+Y** - Redo
- [ ] **Ctrl++** - Zoom in
- [ ] **Ctrl+-** - Zoom out
- [ ] **Delete** - Delete selected element
- [ ] **Ctrl+A** - Select all (if implemented)

**Expected:** All shortcuts work as described

---

## Test Suite 9: Status Bar 📊

Check status bar at bottom:

- [ ] Shows Model ID
- [ ] Shows Model Type
- [ ] Shows selected element name when selected
- [ ] "Show/Hide Palette" button works
- [ ] "Show/Hide Properties" button works

**Expected:** All information displays correctly

---

## Test Suite 10: Error Handling 🚨

### Test 10.1: Invalid Model ID
1. Navigate to `/models/999999/edit` (non-existent)
2. Check error handling

**Expected:**
- [ ] "Model not found" message appears
- [ ] "Back to Models" button works
- [ ] No console errors

### Test 10.2: Network Error
1. Stop backend server
2. Try to save model
3. Check error handling

**Expected:**
- [ ] Error toast appears
- [ ] Meaningful error message
- [ ] Application remains functional

### Test 10.3: Empty Diagram
1. Open editor with new model
2. Don't add any elements
3. Try to save

**Expected:**
- [ ] Empty diagram saves successfully
- [ ] No errors occur

---

## Test Suite 11: Responsive Design 📱

### Test 11.1: Panel Resizing
1. Toggle palette off and on
2. Toggle properties off and on
3. Hide both panels

**Expected:**
- [ ] Canvas resizes to fill space
- [ ] No visual glitches
- [ ] Layout remains functional

### Test 11.2: Window Resize
1. Resize browser window smaller
2. Resize browser window larger
3. Check all components

**Expected:**
- [ ] Components adjust to window size
- [ ] No horizontal scrolling
- [ ] All features accessible

---

## Test Suite 12: Complex Scenarios 🎯

### Test 12.1: Create Business Process Diagram
1. Add Start Event
2. Add Task ("Process Order")
3. Add Gateway
4. Add two more Tasks
5. Add End Event
6. Connect all with links
7. Save

**Expected:**
- [ ] Can create complete process flow
- [ ] All connections work
- [ ] Saves successfully

### Test 12.2: Create Application Architecture
1. Add 3 Application Components
2. Add 2 Application Services
3. Add Data Object
4. Connect components to services
5. Change colors to categorize
6. Add descriptions
7. Save

**Expected:**
- [ ] Can create architecture diagram
- [ ] Properties editable
- [ ] Visual organization works

### Test 12.3: Large Diagram
1. Add 20+ elements
2. Create multiple connections
3. Test auto-layout
4. Test zoom and fit
5. Test save

**Expected:**
- [ ] Performance remains good
- [ ] All operations work
- [ ] Save completes successfully

---

## Test Results Summary 📊

After completing all tests, fill out:

### Passed Tests: ___ / Total: ___

### Critical Issues Found:
1. 
2. 
3. 

### Minor Issues Found:
1. 
2. 
3. 

### Suggestions for Improvement:
1. 
2. 
3. 

---

## Browser Compatibility 🌐

Test in multiple browsers:

- [ ] Chrome/Edge (Latest)
- [ ] Firefox (Latest)
- [ ] Safari (if available)

---

## Performance Metrics 📈

- [ ] Editor loads in < 2 seconds
- [ ] Element addition is instant
- [ ] Save operation < 1 second
- [ ] No lag with 50+ elements
- [ ] Memory usage stable

---

## Final Checklist ✅

- [ ] All core features work
- [ ] No console errors
- [ ] Saves to database correctly
- [ ] UI is responsive
- [ ] Keyboard shortcuts work
- [ ] Error handling works
- [ ] Documentation is accurate
- [ ] Ready for production use

---

## 🎉 Testing Complete!

Once all tests pass, the Visual Editor is **production-ready**!

**Report any issues found during testing for quick fixes.**
