import { useEffect, useRef, useState } from 'react';
import * as go from 'gojs';
import { ReactDiagram } from 'gojs-react';
import './diagram-canvas.css';

interface DiagramCanvasProps {
  modelData?: any;
  onModelChange?: (model: go.Model) => void;
  modelType?: string;
  readOnly?: boolean;
}

export default function DiagramCanvas({
  modelData,
  onModelChange,
  modelType = 'archimate',
  readOnly = false
}: DiagramCanvasProps) {
  const diagramRef = useRef<ReactDiagram>(null);
  const [diagram, setDiagram] = useState<go.Diagram | null>(null);

  // Initialize diagram
  const initDiagram = (): go.Diagram => {
    const $ = go.GraphObject.make;

    const myDiagram = $(go.Diagram, {
      'undoManager.isEnabled': true,
      'allowCopy': !readOnly,
      'allowDelete': !readOnly,
      'allowMove': !readOnly,
      'isReadOnly': readOnly,
      'layout': $(go.LayeredDigraphLayout, {
        direction: 90,
        layerSpacing: 50,
        columnSpacing: 30
      }),
      model: $(go.GraphLinksModel, {
        linkKeyProperty: 'key',
        makeUniqueKeyFunction: (model: go.Model, data: any) => {
          let k = data.key || 1;
          while (model.findNodeDataForKey(k)) k++;
          data.key = k;
          return k;
        },
        makeUniqueLinkKeyFunction: (model: go.GraphLinksModel, data: any) => {
          let k = data.key || -1;
          while (model.findLinkDataForKey(k)) k--;
          data.key = k;
          return k;
        }
      })
    });

    // Define node templates based on model type
    if (modelType === 'archimate') {
      myDiagram.nodeTemplate = createArchiMateNodeTemplate($);
    } else if (modelType === 'bpmn') {
      myDiagram.nodeTemplate = createBPMNNodeTemplate($);
    } else if (modelType === 'uml') {
      myDiagram.nodeTemplate = createUMLNodeTemplate($);
    } else {
      myDiagram.nodeTemplate = createDefaultNodeTemplate($);
    }

    // Define link template
    myDiagram.linkTemplate = $(
      go.Link,
      {
        routing: go.Link.AvoidsNodes,
        curve: go.Link.JumpOver,
        corner: 5,
        toShortLength: 4,
        relinkableFrom: !readOnly,
        relinkableTo: !readOnly,
        reshapable: !readOnly,
        resegmentable: !readOnly
      },
      new go.Binding('points').makeTwoWay(),
      $(
        go.Shape,
        { strokeWidth: 2, stroke: '#6366f1' }
      ),
      $(
        go.Shape,
        { toArrow: 'Standard', strokeWidth: 0, fill: '#6366f1' }
      ),
      $(
        go.Panel,
        'Auto',
        $(
          go.Shape,
          'RoundedRectangle',
          { fill: 'white', stroke: null }
        ),
        $(
          go.TextBlock,
          {
            textAlign: 'center',
            font: '11px sans-serif',
            stroke: '#374151',
            margin: 4,
            editable: !readOnly
          },
          new go.Binding('text', 'label').makeTwoWay()
        )
      )
    );

    // Model change listener
    myDiagram.addModelChangedListener((evt) => {
      if (evt.isTransactionFinished && onModelChange && evt.model) {
        onModelChange(evt.model);
      }
    });

    return myDiagram;
  };

  // Create ArchiMate node template
  const createArchiMateNodeTemplate = ($: any): go.Node => {
    return $(
      go.Node,
      'Auto',
      {
        locationSpot: go.Spot.Center,
        selectionAdorned: true,
        resizable: true,
        resizeObjectName: 'PANEL',
        rotatable: false
      },
      new go.Binding('location', 'loc', go.Point.parse).makeTwoWay(go.Point.stringify),
      new go.Binding('desiredSize', 'size', go.Size.parse).makeTwoWay(go.Size.stringify),
      $(
        go.Shape,
        'RoundedRectangle',
        {
          name: 'PANEL',
          fill: '#e0f2fe',
          stroke: '#0284c7',
          strokeWidth: 2,
          portId: '',
          cursor: 'pointer',
          fromLinkable: true,
          toLinkable: true,
          fromLinkableDuplicates: true,
          toLinkableDuplicates: true,
          fromSpot: go.Spot.AllSides,
          toSpot: go.Spot.AllSides
        },
        new go.Binding('fill', 'color'),
        new go.Binding('stroke', 'borderColor'),
        new go.Binding('figure', 'figure')
      ),
      $(
        go.Panel,
        'Vertical',
        { margin: 8 },
        $(
          go.TextBlock,
          {
            font: 'bold 12px sans-serif',
            stroke: '#0c4a6e',
            margin: new go.Margin(4, 4, 0, 4),
            editable: true,
            textAlign: 'center'
          },
          new go.Binding('text', 'name').makeTwoWay()
        ),
        $(
          go.TextBlock,
          {
            font: '10px sans-serif',
            stroke: '#475569',
            margin: new go.Margin(4, 4, 4, 4),
            editable: true,
            textAlign: 'center',
            maxSize: new go.Size(150, NaN)
          },
          new go.Binding('text', 'type'),
          new go.Binding('visible', 'type', (t) => !!t)
        )
      )
    );
  };

  // Create BPMN node template
  const createBPMNNodeTemplate = ($: any): go.Node => {
    return $(
      go.Node,
      'Auto',
      {
        locationSpot: go.Spot.Center,
        selectionAdorned: true,
        resizable: true,
        resizeObjectName: 'SHAPE'
      },
      new go.Binding('location', 'loc', go.Point.parse).makeTwoWay(go.Point.stringify),
      $(
        go.Shape,
        {
          name: 'SHAPE',
          fill: '#fef3c7',
          stroke: '#f59e0b',
          strokeWidth: 2,
          portId: '',
          fromLinkable: true,
          toLinkable: true
        },
        new go.Binding('figure', 'figure'),
        new go.Binding('fill', 'color')
      ),
      $(
        go.TextBlock,
        {
          font: 'bold 11px sans-serif',
          margin: 8,
          editable: true,
          textAlign: 'center',
          maxSize: new go.Size(120, NaN)
        },
        new go.Binding('text', 'name').makeTwoWay()
      )
    );
  };

  // Create UML node template
  const createUMLNodeTemplate = ($: any): go.Node => {
    return $(
      go.Node,
      'Auto',
      {
        locationSpot: go.Spot.Center,
        selectionAdorned: true,
        resizable: true
      },
      new go.Binding('location', 'loc', go.Point.parse).makeTwoWay(go.Point.stringify),
      $(
        go.Shape,
        'Rectangle',
        {
          fill: '#dbeafe',
          stroke: '#1e40af',
          strokeWidth: 2,
          portId: '',
          fromLinkable: true,
          toLinkable: true
        },
        new go.Binding('fill', 'color')
      ),
      $(
        go.Panel,
        'Vertical',
        { margin: 8 },
        $(
          go.TextBlock,
          {
            font: 'bold 11px sans-serif',
            margin: new go.Margin(4, 4, 2, 4),
            editable: true,
            textAlign: 'center'
          },
          new go.Binding('text', 'name').makeTwoWay()
        ),
        $(
          go.Shape,
          'LineH',
          { stroke: '#1e40af', height: 1, stretch: go.GraphObject.Horizontal }
        ),
        $(
          go.TextBlock,
          {
            font: '10px sans-serif',
            margin: new go.Margin(2, 4, 4, 4),
            editable: true,
            textAlign: 'left',
            maxSize: new go.Size(150, NaN)
          },
          new go.Binding('text', 'properties').makeTwoWay()
        )
      )
    );
  };

  // Create default node template
  const createDefaultNodeTemplate = ($: any): go.Node => {
    return $(
      go.Node,
      'Auto',
      {
        locationSpot: go.Spot.Center,
        selectionAdorned: true,
        resizable: true
      },
      new go.Binding('location', 'loc', go.Point.parse).makeTwoWay(go.Point.stringify),
      $(
        go.Shape,
        'RoundedRectangle',
        {
          fill: '#f3f4f6',
          stroke: '#6b7280',
          strokeWidth: 2,
          portId: '',
          fromLinkable: true,
          toLinkable: true
        },
        new go.Binding('fill', 'color')
      ),
      $(
        go.TextBlock,
        {
          font: 'bold 11px sans-serif',
          margin: 10,
          editable: true,
          textAlign: 'center',
          maxSize: new go.Size(140, NaN)
        },
        new go.Binding('text', 'name').makeTwoWay()
      )
    );
  };

  // Parse model data for initial load
  const getInitialData = () => {
    if (!modelData) {
      return { nodeDataArray: [], linkDataArray: [] };
    }
    
    try {
      // If modelData is a string, parse it
      if (typeof modelData === 'string') {
        return JSON.parse(modelData);
      }
      // If it's already an object with the right structure
      if (modelData.nodeDataArray !== undefined) {
        return modelData;
      }
      // Otherwise return empty
      return { nodeDataArray: [], linkDataArray: [] };
    } catch (error) {
      console.error('Error parsing model data:', error);
      return { nodeDataArray: [], linkDataArray: [] };
    }
  };

  const initialData = getInitialData();

  // Load model data when it changes (after initial load)
  useEffect(() => {
    if (diagram && modelData) {
      try {
        const parsedData = typeof modelData === 'string' ? JSON.parse(modelData) : modelData;
        diagram.model = go.Model.fromJson(parsedData);
      } catch (error) {
        console.error('Error loading model data:', error);
      }
    }
  }, [diagram, modelData]);

  // Handle diagram initialization
  useEffect(() => {
    if (diagramRef.current) {
      const diag = diagramRef.current.getDiagram();
      if (diag) {
        setDiagram(diag);
      }
    }
  }, []);

  return (
    <div className="w-full h-full bg-white border border-gray-200 rounded-lg">
      <ReactDiagram
        ref={diagramRef}
        divClassName="diagram-component"
        initDiagram={initDiagram}
        nodeDataArray={initialData.nodeDataArray}
        linkDataArray={initialData.linkDataArray}
      />
    </div>
  );
}
