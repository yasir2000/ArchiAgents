# ArchiAgents Web App - Quick Integration Guide

## 🚀 Quick Start: Using New Components

### 1. AI Model Generation

**In any page (Projects, Models, Dashboard):**

```tsx
import { useState } from 'react';
import { Wand2 } from 'lucide-react';
import AIGenerationModal from '../components/AIGenerationModal';

function YourPage() {
  const [showAIModal, setShowAIModal] = useState(false);
  const projectId = 'your-project-id';

  return (
    <>
      {/* Trigger Button */}
      <button
        onClick={() => setShowAIModal(true)}
        className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 flex items-center space-x-2"
      >
        <Wand2 className="w-4 h-4" />
        <span>Generate with AI</span>
      </button>

      {/* Modal */}
      <AIGenerationModal
        isOpen={showAIModal}
        onClose={() => setShowAIModal(false)}
        projectId={projectId}
        onSuccess={(modelId) => {
          console.log('Generated model:', modelId);
          // Navigate to editor or refresh list
        }}
      />
    </>
  );
}
```

---

### 2. Export Model

**In ModelEditorPage or ModelDetailPage:**

```tsx
import { useState } from 'react';
import { Download } from 'lucide-react';
import ExportDialog from '../components/ExportDialog';

function ModelPage() {
  const [showExport, setShowExport] = useState(false);
  const modelId = 'your-model-id';
  const modelName = 'Business Architecture';

  return (
    <>
      {/* Trigger Button */}
      <button
        onClick={() => setShowExport(true)}
        className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 flex items-center space-x-2"
      >
        <Download className="w-4 h-4" />
        <span>Export</span>
      </button>

      {/* Dialog */}
      <ExportDialog
        isOpen={showExport}
        onClose={() => setShowExport(false)}
        modelId={modelId}
        modelName={modelName}
      />
    </>
  );
}
```

---

### 3. Import Model

**In ModelsPage or ProjectDetailPage:**

```tsx
import { useState } from 'react';
import { Upload } from 'lucide-react';
import ModelImportDialog from '../components/ModelImportDialog';

function ModelsPage() {
  const [showImport, setShowImport] = useState(false);
  const projectId = 'your-project-id';

  return (
    <>
      {/* Trigger Button */}
      <button
        onClick={() => setShowImport(true)}
        className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 flex items-center space-x-2"
      >
        <Upload className="w-4 h-4" />
        <span>Import Model</span>
      </button>

      {/* Dialog */}
      <ModelImportDialog
        isOpen={showImport}
        onClose={() => setShowImport(false)}
        projectId={projectId}
        onSuccess={(modelId) => {
          console.log('Imported model:', modelId);
          // Refresh model list
        }}
      />
    </>
  );
}
```

---

### 4. Collaboration Panel

**In ModelEditorPage (sidebar):**

```tsx
import CollaborationPanel from '../components/CollaborationPanel';

function ModelEditorPage() {
  const { id } = useParams();
  const projectId = 'your-project-id';

  return (
    <div className="flex h-screen">
      {/* Main Editor */}
      <div className="flex-1 p-6">
        {/* Your GoJS canvas or editor */}
      </div>

      {/* Collaboration Sidebar */}
      <div className="w-80 border-l border-gray-200">
        <CollaborationPanel 
          modelId={id} 
          projectId={projectId} 
        />
      </div>
    </div>
  );
}
```

---

### 5. Global Search

**Already integrated in Layout! Just use Ctrl+K or:**

```tsx
// Manual trigger in any component
import { useState } from 'react';
import { Search } from 'lucide-react';
import SearchComponent from '../components/SearchComponent';

function YourComponent() {
  const [searchOpen, setSearchOpen] = useState(false);

  return (
    <>
      <button onClick={() => setSearchOpen(true)}>
        <Search className="w-5 h-5" />
      </button>

      <SearchComponent 
        isOpen={searchOpen} 
        onClose={() => setSearchOpen(false)} 
      />
    </>
  );
}
```

---

### 6. Notifications

**Already integrated in Layout via NotificationBellIcon!**

Access from anywhere:
- Bell icon in header shows unread count
- Click to open notification center
- Real-time updates every 30 seconds

---

## 📍 Navigation Routes

All routes are already configured in `App.tsx`:

```tsx
// Public routes
/login              → LoginPage
/register           → RegisterPage

// Protected routes (requires authentication)
/                   → DashboardPage
/projects           → ProjectsPage
/projects/:id       → ProjectDetailPage
/models             → ModelsPage
/models/:id/edit    → ModelEditorPage
/settings           → SettingsPage        ✨ NEW
/team               → TeamManagementPage  ✨ NEW
```

---

## 🎨 Component Props Reference

### AIGenerationModal
```tsx
interface Props {
  isOpen: boolean;           // Control visibility
  onClose: () => void;       // Close handler
  projectId: string;         // Target project
  onSuccess: (modelId: string) => void;  // Success callback
}
```

### ExportDialog
```tsx
interface Props {
  isOpen: boolean;
  onClose: () => void;
  modelId: string;           // Model to export
  modelName: string;         // For filename
}
```

### ModelImportDialog
```tsx
interface Props {
  isOpen: boolean;
  onClose: () => void;
  projectId: string;         // Target project
  onSuccess: (modelId: string) => void;
}
```

### SearchComponent
```tsx
interface Props {
  isOpen: boolean;
  onClose: () => void;
}
```

### CollaborationPanel
```tsx
interface Props {
  modelId: string;           // Current model
  projectId: string;         // Parent project
}
```

---

## 🔧 Common Patterns

### Modal State Management
```tsx
const [isOpen, setIsOpen] = useState(false);

// Open
<button onClick={() => setIsOpen(true)}>Open</button>

// Component
<Component 
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
  onSuccess={(result) => {
    // Handle success
    setIsOpen(false);
  }}
/>
```

### Error Handling
```tsx
// Components handle errors internally and show toast
// You just need to provide callbacks:

onSuccess={(result) => {
  // Success case - update UI
  toast.success('Operation successful!');
}}

onError={(error) => {  // Optional
  // Components already show error toasts
  // This is for additional handling
}}
```

### Loading States
```tsx
// Components manage their own loading states
// No need to track loading externally
// Just provide the data they need
```

---

## 🎯 Feature Combination Examples

### Complete Model Workflow
```tsx
function ModelsWorkflow() {
  const [showAI, setShowAI] = useState(false);
  const [showImport, setShowImport] = useState(false);
  const [showExport, setShowExport] = useState(false);
  const [selectedModel, setSelectedModel] = useState(null);

  return (
    <div className="p-6">
      {/* Action Bar */}
      <div className="flex space-x-3 mb-6">
        <button onClick={() => setShowAI(true)}>
          🤖 Generate with AI
        </button>
        <button onClick={() => setShowImport(true)}>
          📥 Import Model
        </button>
        {selectedModel && (
          <button onClick={() => setShowExport(true)}>
            📤 Export Model
          </button>
        )}
      </div>

      {/* Model List */}
      <div className="grid grid-cols-3 gap-4">
        {/* Your model cards */}
      </div>

      {/* Modals */}
      <AIGenerationModal
        isOpen={showAI}
        onClose={() => setShowAI(false)}
        projectId={projectId}
        onSuccess={(id) => {
          // Refresh models
          fetchModels();
        }}
      />

      <ModelImportDialog
        isOpen={showImport}
        onClose={() => setShowImport(false)}
        projectId={projectId}
        onSuccess={(id) => {
          fetchModels();
        }}
      />

      <ExportDialog
        isOpen={showExport}
        onClose={() => setShowExport(false)}
        modelId={selectedModel?.id}
        modelName={selectedModel?.name}
      />
    </div>
  );
}
```

---

## 📦 Import Statements

### Common Imports
```tsx
// Components
import AIGenerationModal from '../components/AIGenerationModal';
import ExportDialog from '../components/ExportDialog';
import ModelImportDialog from '../components/ModelImportDialog';
import SearchComponent from '../components/SearchComponent';
import CollaborationPanel from '../components/CollaborationPanel';
import { NotificationBellIcon } from '../components/NotificationCenter';

// Icons
import { Wand2, Download, Upload, Search, Bell } from 'lucide-react';

// Hooks
import { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

// Store
import { useAuthStore } from '../stores/authStore';

// Toast
import { toast } from 'react-hot-toast';
```

---

## 🎨 Styling Guidelines

### Button Styles
```tsx
// Primary Action
className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"

// Secondary Action  
className="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50"

// Danger Action
className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700"

// AI Action (Purple)
className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700"

// Export (Green)
className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"

// Import (Indigo)
className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700"
```

### Icon Sizes
```tsx
// Small (in buttons, lists)
<Icon className="w-4 h-4" />

// Medium (standalone)
<Icon className="w-5 h-5" />

// Large (headers, empty states)
<Icon className="w-6 h-6" />

// Extra Large (empty states)
<Icon className="w-12 h-12" />
```

---

## 🚀 Performance Tips

1. **Lazy Load Modals**: Only render when `isOpen={true}`
2. **Debounce Search**: Already implemented (300ms)
3. **Virtualize Large Lists**: Use `react-window` for 100+ items
4. **Memoize Callbacks**: Use `useCallback` for event handlers
5. **Cache API Responses**: Use React Query for data fetching

---

## 🐛 Troubleshooting

### Modal Not Showing
```tsx
// Check z-index in parent
<div className="relative z-10"> {/* Parent */}
  <Modal isOpen={true} /> {/* Modal has z-50 */}
</div>
```

### API Errors
```tsx
// Check apiClient configuration
// Ensure token is set in authStore
// Verify backend is running
```

### TypeScript Errors
```tsx
// Update types in src/types/index.ts
// Ensure all props match interface definitions
```

---

## 📚 Additional Resources

- **Full Documentation**: `WEB_APP_ADVANCED_FEATURES_COMPLETE.md`
- **Backend API**: `WEB_APP_IMPLEMENTATION_GUIDE.md`
- **Component Code**: `web_app/frontend/src/components/`
- **Page Examples**: `web_app/frontend/src/pages/`

---

**Happy Coding! 🎉**

All components are production-ready and fully typed with TypeScript.
