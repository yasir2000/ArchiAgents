# Visual Editor - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Start the Application

```bash
# Terminal 1: Start Backend
cd web_app/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py

# Terminal 2: Start Frontend
cd web_app/frontend
npm install
npm run dev
```

### Step 2: Access the Editor

1. Open browser: `http://localhost:3000`
2. Login with your credentials (or create account)
3. Navigate to **Models** page
4. Click on any model or create a new one
5. Click **Edit** button

---

## 🎨 Using the Visual Editor

### Creating Diagrams

#### 1. Add Elements from Palette (Left Panel)
- Browse elements by category
- Use search to find specific elements
- Click an element to add it to the canvas
- Element will be added to the diagram center

#### 2. Position and Resize
- **Drag** elements to move them
- **Resize** by dragging corner handles
- **Multi-select** by holding Ctrl/Cmd and clicking

#### 3. Create Connections
- **Click and drag** from one element to another
- Links automatically route around other elements
- **Double-click** link label to edit text

#### 4. Edit Properties (Right Panel)
- Click an element to select it
- Properties panel shows editable fields:
  - Name
  - Type
  - Description
  - Colors (fill and border)
  - Documentation
- Changes apply immediately

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+S` | Save model |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` | Redo |
| `Ctrl++` | Zoom in |
| `Ctrl+-` | Zoom out |
| `Delete` | Delete selected |
| `Ctrl+A` | Select all |
| `Ctrl+C` | Copy |
| `Ctrl+V` | Paste |

---

## 🛠️ Toolbar Actions

### File Operations
- **Save** - Save current model to backend
- **Export** - Export model (coming soon)

### Edit Operations
- **Undo** - Undo last action
- **Redo** - Redo undone action
- **Delete** - Delete selected elements

### View Controls
- **Zoom In** - Increase zoom level
- **Zoom Out** - Decrease zoom level
- **Fit to Screen** - Fit all elements in view

### Layout Controls
- **Auto Layout** - Automatically organize elements
- **Toggle Grid** - Show/hide background grid
- **Preview** - Preview mode (coming soon)

---

## 📊 Model Types

### ArchiMate Diagrams
Best for: Enterprise Architecture, Business Models

**Layers:**
- **Strategy** - Capabilities, Resources, Value Streams
- **Business** - Processes, Functions, Actors, Services
- **Application** - Components, Services, Interfaces, Data
- **Technology** - Nodes, Devices, Software, Artifacts

**Example Use Cases:**
- Application landscape diagrams
- Business process models
- Technology stack visualization
- Capability maps

### BPMN Diagrams
Best for: Business Process Modeling

**Elements:**
- **Activities** - Tasks, Sub-processes
- **Gateways** - Decision points
- **Events** - Start, End, Intermediate
- **Swim Lanes** - Pools, Lanes

**Example Use Cases:**
- Process flow documentation
- Workflow automation design
- Business process optimization
- Cross-functional processes

### UML Diagrams
Best for: Software Design, System Modeling

**Elements:**
- **Structure** - Classes, Interfaces, Components, Packages
- **Behavior** - Use Cases, Actors, States

**Example Use Cases:**
- Class diagrams
- Component architecture
- Use case diagrams
- State machines

---

## 💡 Tips & Best Practices

### Organizing Your Diagram

1. **Use Layers Appropriately**
   - Keep related elements together
   - Use ArchiMate layers to separate concerns
   - Group business and technical elements

2. **Consistent Naming**
   - Use clear, descriptive names
   - Follow naming conventions
   - Be consistent with terminology

3. **Color Coding**
   - Use colors to group related elements
   - Maintain consistency across diagrams
   - Don't overuse colors

4. **Layout**
   - Use Auto Layout for quick organization
   - Manually adjust for clarity
   - Minimize crossing links
   - Use pools/lanes for process organization

### Performance Tips

1. **Large Diagrams**
   - Break complex diagrams into smaller views
   - Use sub-processes for BPMN
   - Create multiple related models

2. **Saving**
   - Save frequently (Ctrl+S)
   - Auto-save is triggered on changes
   - Check for save confirmation

---

## 🎯 Common Tasks

### Task 1: Create a Simple Business Process

1. Select **BPMN** model type
2. Add **Start Event** from palette
3. Add **Task** element
4. Add **End Event**
5. Connect: Start → Task → End
6. Edit task name in properties
7. Save model

### Task 2: Build an Application Architecture

1. Select **ArchiMate** model type
2. Add **Application Components** from palette
3. Position components logically
4. Add **Application Services**
5. Connect components with services
6. Add **Data Objects** if needed
7. Color-code by domain
8. Save model

### Task 3: Design a Class Diagram

1. Select **UML** model type
2. Add **Class** elements
3. Edit class names and properties
4. Add **Interface** elements
5. Connect classes with relationships
6. Add attributes in properties panel
7. Use Auto Layout
8. Save model

---

## ❓ Troubleshooting

### Element Not Appearing
- Check if element is outside visible area
- Use "Fit to Screen" to see all elements
- Check zoom level

### Cannot Edit Properties
- Ensure element is selected (blue border)
- Check if properties panel is visible
- Try clicking element again

### Save Not Working
- Check backend connection (http://localhost:8000)
- Verify you're logged in
- Check browser console for errors
- Check network tab in DevTools

### Performance Issues
- Reduce number of elements
- Close unused panels
- Clear browser cache
- Restart application

---

## 🔗 Additional Resources

- [Full Documentation](./VISUAL_EDITOR_COMPLETE.md)
- [Backend API Guide](../../backend/README.md)
- [GoJS Documentation](https://gojs.net/latest/index.html)
- [ArchiMate Specification](https://pubs.opengroup.org/architecture/archimate3-doc/)
- [BPMN Specification](https://www.omg.org/spec/BPMN/2.0/)

---

## 🆘 Getting Help

1. **Check Documentation** - Read full documentation
2. **Backend Logs** - Check `web_app/backend/main.py` output
3. **Frontend Console** - Open browser DevTools (F12)
4. **Network Tab** - Check API calls and responses
5. **GitHub Issues** - Report bugs and request features

---

**Happy Modeling! 🎨**

Start creating professional architecture diagrams in minutes!
