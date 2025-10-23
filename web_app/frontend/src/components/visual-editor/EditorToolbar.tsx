import { Save, Download, Undo, Redo, ZoomIn, ZoomOut, Maximize2, Grid, Layout, Eye, Trash2 } from 'lucide-react';

interface EditorToolbarProps {
  onSave: () => void;
  onExport: () => void;
  onUndo: () => void;
  onRedo: () => void;
  onZoomIn: () => void;
  onZoomOut: () => void;
  onFitToScreen: () => void;
  onToggleGrid: () => void;
  onAutoLayout: () => void;
  onPreview: () => void;
  onDelete: () => void;
  canUndo: boolean;
  canRedo: boolean;
  gridVisible: boolean;
  zoom: number;
}

export default function EditorToolbar({
  onSave,
  onExport,
  onUndo,
  onRedo,
  onZoomIn,
  onZoomOut,
  onFitToScreen,
  onToggleGrid,
  onAutoLayout,
  onPreview,
  onDelete,
  canUndo,
  canRedo,
  gridVisible,
  zoom
}: EditorToolbarProps) {
  const ToolButton = ({ 
    icon, 
    label, 
    onClick, 
    disabled = false,
    variant = 'default'
  }: { 
    icon: React.ReactNode; 
    label: string; 
    onClick: () => void; 
    disabled?: boolean;
    variant?: 'default' | 'primary' | 'danger';
  }) => {
    const baseClasses = "p-2 rounded hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors";
    const variantClasses = {
      default: 'text-gray-700',
      primary: 'text-indigo-600 hover:bg-indigo-50',
      danger: 'text-red-600 hover:bg-red-50'
    };

    return (
      <button
        onClick={onClick}
        disabled={disabled}
        className={`${baseClasses} ${variantClasses[variant]}`}
        title={label}
      >
        {icon}
      </button>
    );
  };

  return (
    <div className="bg-white border-b border-gray-200 px-4 py-2">
      <div className="flex items-center justify-between">
        {/* Left section - File operations */}
        <div className="flex items-center space-x-1">
          <ToolButton
            icon={<Save className="w-5 h-5" />}
            label="Save (Ctrl+S)"
            onClick={onSave}
            variant="primary"
          />
          <ToolButton
            icon={<Download className="w-5 h-5" />}
            label="Export"
            onClick={onExport}
          />
          <div className="w-px h-6 bg-gray-300 mx-2" />
          <ToolButton
            icon={<Undo className="w-5 h-5" />}
            label="Undo (Ctrl+Z)"
            onClick={onUndo}
            disabled={!canUndo}
          />
          <ToolButton
            icon={<Redo className="w-5 h-5" />}
            label="Redo (Ctrl+Y)"
            onClick={onRedo}
            disabled={!canRedo}
          />
        </div>

        {/* Center section - Layout and view */}
        <div className="flex items-center space-x-1">
          <ToolButton
            icon={<Layout className="w-5 h-5" />}
            label="Auto Layout"
            onClick={onAutoLayout}
          />
          <ToolButton
            icon={<Grid className="w-5 h-5" />}
            label={gridVisible ? "Hide Grid" : "Show Grid"}
            onClick={onToggleGrid}
          />
          <ToolButton
            icon={<Eye className="w-5 h-5" />}
            label="Preview"
            onClick={onPreview}
          />
          <div className="w-px h-6 bg-gray-300 mx-2" />
          <ToolButton
            icon={<Trash2 className="w-5 h-5" />}
            label="Delete Selected"
            onClick={onDelete}
            variant="danger"
          />
        </div>

        {/* Right section - Zoom controls */}
        <div className="flex items-center space-x-1">
          <ToolButton
            icon={<ZoomOut className="w-5 h-5" />}
            label="Zoom Out (Ctrl+-)"
            onClick={onZoomOut}
          />
          <div className="px-3 py-1 bg-gray-100 rounded text-sm font-medium text-gray-700 min-w-[60px] text-center">
            {Math.round(zoom * 100)}%
          </div>
          <ToolButton
            icon={<ZoomIn className="w-5 h-5" />}
            label="Zoom In (Ctrl++)"
            onClick={onZoomIn}
          />
          <ToolButton
            icon={<Maximize2 className="w-5 h-5" />}
            label="Fit to Screen"
            onClick={onFitToScreen}
          />
        </div>
      </div>
    </div>
  );
}
