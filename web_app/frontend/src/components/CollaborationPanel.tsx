import { useState, useEffect } from 'react';
import { Users, Activity, MessageCircle, User as UserIcon, Circle } from 'lucide-react';
import { useCollaborationStore } from '../stores/collaborationStore';
import { useAuthStore } from '../stores/authStore';

interface CollaborationPanelProps {
  modelId: string;
  projectId: string;
}

interface Participant {
  id: string;
  username: string;
  full_name: string;
  role: string;
  status: 'active' | 'idle' | 'offline';
  cursor?: {
    x: number;
    y: number;
  };
  lastActivity: string;
}

interface ActivityEvent {
  id: string;
  user: string;
  action: string;
  timestamp: string;
  details?: string;
}

export default function CollaborationPanel({ modelId, projectId }: CollaborationPanelProps) {
  const { user } = useAuthStore();
  const {
    participants,
    activityFeed,
    isConnected,
    connect,
    disconnect,
    sendUpdate,
  } = useCollaborationStore();

  const [activeTab, setActiveTab] = useState<'participants' | 'activity'>('participants');
  const [localParticipants, setLocalParticipants] = useState<Participant[]>([]);
  const [localActivity, setLocalActivity] = useState<ActivityEvent[]>([]);

  useEffect(() => {
    // Connect to WebSocket for real-time collaboration
    if (modelId && user) {
      connect(modelId, user.id.toString());
    }

    return () => {
      disconnect();
    };
  }, [modelId, user]);

  useEffect(() => {
    // Simulate participants for demonstration
    setLocalParticipants([
      {
        id: user?.id?.toString() || '1',
        username: user?.username || 'currentuser',
        full_name: user?.full_name || 'Current User',
        role: user?.role || 'architect',
        status: 'active',
        lastActivity: new Date().toISOString(),
      },
    ]);

    // Simulate activity feed
    setLocalActivity([
      {
        id: '1',
        user: user?.full_name || 'You',
        action: 'opened',
        timestamp: new Date().toISOString(),
        details: 'the model for editing',
      },
    ]);
  }, [user]);

  const getStatusColor = (status: Participant['status']) => {
    switch (status) {
      case 'active':
        return 'bg-green-500';
      case 'idle':
        return 'bg-yellow-500';
      case 'offline':
        return 'bg-gray-400';
      default:
        return 'bg-gray-400';
    }
  };

  const getStatusLabel = (status: Participant['status']) => {
    switch (status) {
      case 'active':
        return 'Active';
      case 'idle':
        return 'Idle';
      case 'offline':
        return 'Offline';
      default:
        return 'Unknown';
    }
  };

  const getRoleColor = (role: string) => {
    const colors: Record<string, string> = {
      admin: 'bg-red-100 text-red-700',
      architect: 'bg-purple-100 text-purple-700',
      contributor: 'bg-blue-100 text-blue-700',
      reviewer: 'bg-green-100 text-green-700',
      viewer: 'bg-gray-100 text-gray-700',
    };
    return colors[role] || 'bg-gray-100 text-gray-700';
  };

  const getTimeAgo = (dateString: string) => {
    const now = new Date();
    const date = new Date(dateString);
    const seconds = Math.floor((now.getTime() - date.getTime()) / 1000);

    if (seconds < 60) return 'just now';
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`;
    if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`;
    return date.toLocaleDateString();
  };

  const activeParticipants = localParticipants.filter((p) => p.status === 'active');

  return (
    <div className="bg-white rounded-lg shadow h-full flex flex-col">
      {/* Header */}
      <div className="p-4 border-b border-gray-200">
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-900">Collaboration</h3>
          <div className="flex items-center space-x-2">
            <Circle
              className={`w-2 h-2 ${isConnected ? 'text-green-500' : 'text-red-500'} fill-current`}
            />
            <span className="text-xs text-gray-600">
              {isConnected ? 'Connected' : 'Disconnected'}
            </span>
          </div>
        </div>

        {/* Tabs */}
        <div className="flex space-x-2">
          <button
            onClick={() => setActiveTab('participants')}
            className={`flex-1 py-2 px-3 rounded-lg text-sm font-medium transition-colors ${
              activeTab === 'participants'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            <div className="flex items-center justify-center space-x-2">
              <Users className="w-4 h-4" />
              <span>
                Users ({activeParticipants.length})
              </span>
            </div>
          </button>
          <button
            onClick={() => setActiveTab('activity')}
            className={`flex-1 py-2 px-3 rounded-lg text-sm font-medium transition-colors ${
              activeTab === 'activity'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            <div className="flex items-center justify-center space-x-2">
              <Activity className="w-4 h-4" />
              <span>Activity</span>
            </div>
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="flex-1 overflow-y-auto p-4">
        {activeTab === 'participants' ? (
          <div className="space-y-3">
            {localParticipants.length === 0 ? (
              <div className="text-center py-8">
                <Users className="w-12 h-12 text-gray-300 mx-auto mb-2" />
                <p className="text-sm text-gray-500">No active participants</p>
              </div>
            ) : (
              localParticipants.map((participant) => (
                <div
                  key={participant.id}
                  className="flex items-start space-x-3 p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
                >
                  {/* Avatar */}
                  <div className="relative flex-shrink-0">
                    <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold">
                      {participant.full_name.charAt(0).toUpperCase()}
                    </div>
                    <div
                      className={`absolute -bottom-1 -right-1 w-3 h-3 rounded-full border-2 border-white ${getStatusColor(
                        participant.status
                      )}`}
                      title={getStatusLabel(participant.status)}
                    />
                  </div>

                  {/* Info */}
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center space-x-2">
                      <p className="text-sm font-semibold text-gray-900 truncate">
                        {participant.full_name}
                        {participant.id === user?.id?.toString() && (
                          <span className="ml-1 text-xs text-blue-600">(You)</span>
                        )}
                      </p>
                    </div>
                    <p className="text-xs text-gray-600">@{participant.username}</p>
                    <div className="flex items-center space-x-2 mt-2">
                      <span
                        className={`text-xs px-2 py-0.5 rounded-full font-medium ${getRoleColor(
                          participant.role
                        )}`}
                      >
                        {participant.role}
                      </span>
                      <span className="text-xs text-gray-500">
                        {getTimeAgo(participant.lastActivity)}
                      </span>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        ) : (
          <div className="space-y-3">
            {localActivity.length === 0 ? (
              <div className="text-center py-8">
                <Activity className="w-12 h-12 text-gray-300 mx-auto mb-2" />
                <p className="text-sm text-gray-500">No recent activity</p>
              </div>
            ) : (
              localActivity.map((event) => (
                <div
                  key={event.id}
                  className="flex items-start space-x-3 p-3 bg-gray-50 rounded-lg"
                >
                  <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center flex-shrink-0">
                    <Activity className="w-4 h-4 text-blue-600" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm text-gray-900">
                      <span className="font-semibold">{event.user}</span>{' '}
                      <span className="text-gray-600">{event.action}</span>{' '}
                      {event.details && (
                        <span className="text-gray-600">{event.details}</span>
                      )}
                    </p>
                    <p className="text-xs text-gray-500 mt-1">
                      {getTimeAgo(event.timestamp)}
                    </p>
                  </div>
                </div>
              ))
            )}
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="p-4 border-t border-gray-200">
        <div className="flex items-center space-x-2 text-xs text-gray-600">
          <MessageCircle className="w-4 h-4" />
          <span>Real-time collaboration enabled</span>
        </div>
      </div>
    </div>
  );
}

// Cursor Component for showing other users' cursors
export function CollaborationCursor({
  username,
  color,
  x,
  y,
}: {
  username: string;
  color: string;
  x: number;
  y: number;
}) {
  return (
    <div
      className="absolute pointer-events-none z-50 transition-all duration-100"
      style={{
        left: `${x}px`,
        top: `${y}px`,
        transform: 'translate(-50%, -50%)',
      }}
    >
      {/* Cursor pointer */}
      <svg
        width="20"
        height="20"
        viewBox="0 0 20 20"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M3 3L17 10L10 11L8 17L3 3Z"
          fill={color}
          stroke="white"
          strokeWidth="2"
        />
      </svg>
      {/* Username label */}
      <div
        className="absolute top-5 left-5 px-2 py-1 rounded text-white text-xs font-semibold whitespace-nowrap shadow-lg"
        style={{ backgroundColor: color }}
      >
        {username}
      </div>
    </div>
  );
}
