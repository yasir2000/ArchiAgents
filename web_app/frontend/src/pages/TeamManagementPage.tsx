import { useState, useEffect } from 'react';
import {
  Users,
  UserPlus,
  Shield,
  Mail,
  Trash2,
  Edit2,
  Check,
  X,
  Loader2,
  Crown,
  Eye,
  FileEdit,
  Search,
} from 'lucide-react';
import { apiClient } from '../lib/api-client';
import { useAuthStore } from '../stores/authStore';
import { toast } from 'react-hot-toast';

interface TeamMember {
  id: string;
  username: string;
  email: string;
  full_name: string;
  role: 'admin' | 'architect' | 'contributor' | 'reviewer' | 'viewer';
  created_at: string;
  last_active?: string;
}

const ROLE_INFO = {
  admin: {
    label: 'Administrator',
    icon: Crown,
    color: 'red',
    description: 'Full system access, user management, and configuration',
  },
  architect: {
    label: 'Architect',
    icon: Shield,
    color: 'purple',
    description: 'Create and manage all architecture models and projects',
  },
  contributor: {
    label: 'Contributor',
    icon: FileEdit,
    color: 'blue',
    description: 'Create and edit models, collaborate with team',
  },
  reviewer: {
    label: 'Reviewer',
    icon: Check,
    color: 'green',
    description: 'Review and approve models, provide feedback',
  },
  viewer: {
    label: 'Viewer',
    icon: Eye,
    color: 'gray',
    description: 'Read-only access to view models and documentation',
  },
};

export default function TeamManagementPage() {
  const { user } = useAuthStore();
  const [members, setMembers] = useState<TeamMember[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [showInviteModal, setShowInviteModal] = useState(false);
  const [editingMember, setEditingMember] = useState<string | null>(null);

  // Check if user is admin
  const isAdmin = user?.role === 'admin';

  useEffect(() => {
    if (!isAdmin) {
      toast.error('Access denied: Administrator role required');
      return;
    }
    fetchTeamMembers();
  }, [isAdmin]);

  const fetchTeamMembers = async () => {
    setIsLoading(true);
    try {
      // This would be replaced with actual API endpoint
      // For now, simulating with sample data
      const response = await apiClient.get('/users');
      setMembers(response.data || []);
    } catch (error) {
      console.error('Failed to fetch team members:', error);
      // Sample data for demonstration
      setMembers([
        {
          id: '1',
          username: 'admin',
          email: 'admin@archiagents.com',
          full_name: 'System Administrator',
          role: 'admin',
          created_at: new Date().toISOString(),
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleRoleChange = async (memberId: string, newRole: string) => {
    try {
      await apiClient.put(`/users/${memberId}/role`, { role: newRole });
      toast.success('Role updated successfully');
      fetchTeamMembers();
      setEditingMember(null);
    } catch (error) {
      toast.error('Failed to update role');
    }
  };

  const handleRemoveMember = async (memberId: string) => {
    if (!window.confirm('Are you sure you want to remove this team member?')) {
      return;
    }

    try {
      await apiClient.delete(`/users/${memberId}`);
      toast.success('Team member removed');
      fetchTeamMembers();
    } catch (error) {
      toast.error('Failed to remove team member');
    }
  };

  const filteredMembers = members.filter(
    (member) =>
      member.username.toLowerCase().includes(searchQuery.toLowerCase()) ||
      member.email.toLowerCase().includes(searchQuery.toLowerCase()) ||
      member.full_name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  if (!isAdmin) {
    return (
      <div className="p-6">
        <div className="bg-red-50 border border-red-200 rounded-lg p-8 text-center">
          <Shield className="w-16 h-16 text-red-600 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-red-900 mb-2">Access Denied</h2>
          <p className="text-red-700">
            You need administrator privileges to access team management.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Team Management</h1>
          <p className="text-gray-600 mt-2">Manage team members, roles, and permissions</p>
        </div>
        <button
          onClick={() => setShowInviteModal(true)}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors flex items-center space-x-2"
        >
          <UserPlus className="w-5 h-5" />
          <span>Invite Member</span>
        </button>
      </div>

      {/* Search */}
      <div className="bg-white rounded-lg shadow p-4">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by name, email, or username..."
            className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
      </div>

      {/* Role Legend */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">Role Descriptions</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {Object.entries(ROLE_INFO).map(([role, info]) => {
            const Icon = info.icon;
            return (
              <div key={role} className="flex items-start space-x-3 p-3 bg-gray-50 rounded-lg">
                <Icon className={`w-5 h-5 text-${info.color}-600 flex-shrink-0 mt-0.5`} />
                <div>
                  <p className="font-medium text-gray-900">{info.label}</p>
                  <p className="text-xs text-gray-600 mt-1">{info.description}</p>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Team Members List */}
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-semibold text-gray-900">
            Team Members ({filteredMembers.length})
          </h2>
        </div>

        {isLoading ? (
          <div className="flex items-center justify-center py-12">
            <Loader2 className="w-8 h-8 text-blue-600 animate-spin" />
          </div>
        ) : (
          <div className="divide-y divide-gray-200">
            {filteredMembers.map((member) => {
              const roleInfo = ROLE_INFO[member.role];
              const RoleIcon = roleInfo.icon;
              const isEditing = editingMember === member.id;
              const isCurrentUser = user?.id === member.id;

              return (
                <div key={member.id} className="p-6 hover:bg-gray-50 transition-colors">
                  <div className="flex items-start justify-between">
                    <div className="flex items-start space-x-4 flex-1">
                      {/* Avatar */}
                      <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold text-lg">
                        {member.full_name.charAt(0).toUpperCase()}
                      </div>

                      {/* Info */}
                      <div className="flex-1">
                        <div className="flex items-center space-x-3">
                          <h3 className="text-lg font-semibold text-gray-900">
                            {member.full_name}
                            {isCurrentUser && (
                              <span className="ml-2 text-xs text-blue-600 font-normal">
                                (You)
                              </span>
                            )}
                          </h3>
                        </div>
                        <p className="text-sm text-gray-600 mt-1">@{member.username}</p>
                        <div className="flex items-center space-x-1 text-sm text-gray-500 mt-1">
                          <Mail className="w-4 h-4" />
                          <span>{member.email}</span>
                        </div>

                        {/* Role Badge/Editor */}
                        <div className="mt-3">
                          {isEditing ? (
                            <div className="flex items-center space-x-2">
                              <select
                                defaultValue={member.role}
                                onChange={(e) => handleRoleChange(member.id, e.target.value)}
                                className="px-3 py-1 border border-gray-300 rounded text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                              >
                                {Object.entries(ROLE_INFO).map(([role, info]) => (
                                  <option key={role} value={role}>
                                    {info.label}
                                  </option>
                                ))}
                              </select>
                              <button
                                onClick={() => setEditingMember(null)}
                                className="p-1 text-gray-400 hover:text-gray-600"
                              >
                                <X className="w-4 h-4" />
                              </button>
                            </div>
                          ) : (
                            <div className="flex items-center space-x-2">
                              <div
                                className={`flex items-center space-x-2 px-3 py-1 bg-${roleInfo.color}-100 text-${roleInfo.color}-700 rounded-full text-sm`}
                              >
                                <RoleIcon className="w-4 h-4" />
                                <span className="font-medium">{roleInfo.label}</span>
                              </div>
                            </div>
                          )}
                        </div>

                        <p className="text-xs text-gray-500 mt-2">
                          Joined {new Date(member.created_at).toLocaleDateString()}
                        </p>
                      </div>
                    </div>

                    {/* Actions */}
                    {!isCurrentUser && (
                      <div className="flex items-center space-x-2">
                        <button
                          onClick={() =>
                            setEditingMember(isEditing ? null : member.id)
                          }
                          className="p-2 text-gray-400 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                          title="Edit role"
                        >
                          <Edit2 className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => handleRemoveMember(member.id)}
                          className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                          title="Remove member"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}

            {filteredMembers.length === 0 && (
              <div className="py-12 text-center">
                <Users className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                <p className="text-gray-500">No team members found</p>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Invite Modal */}
      {showInviteModal && (
        <InviteModal onClose={() => setShowInviteModal(false)} onSuccess={fetchTeamMembers} />
      )}
    </div>
  );
}

// Invite Modal Component
function InviteModal({
  onClose,
  onSuccess,
}: {
  onClose: () => void;
  onSuccess: () => void;
}) {
  const [formData, setFormData] = useState({
    email: '',
    role: 'viewer' as keyof typeof ROLE_INFO,
    message: '',
  });
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      await apiClient.post('/users/invite', formData);
      toast.success('Invitation sent successfully!');
      onSuccess();
      onClose();
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to send invitation');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg shadow-xl max-w-md w-full">
        <div className="p-6 border-b border-gray-200">
          <h2 className="text-2xl font-bold text-gray-900">Invite Team Member</h2>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Email Address *
            </label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="colleague@example.com"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Role *</label>
            <select
              value={formData.role}
              onChange={(e) =>
                setFormData({ ...formData, role: e.target.value as keyof typeof ROLE_INFO })
              }
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            >
              {Object.entries(ROLE_INFO).map(([role, info]) => (
                <option key={role} value={role}>
                  {info.label}
                </option>
              ))}
            </select>
            <p className="text-xs text-gray-500 mt-1">
              {ROLE_INFO[formData.role].description}
            </p>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Message (Optional)
            </label>
            <textarea
              value={formData.message}
              onChange={(e) => setFormData({ ...formData, message: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent h-24 resize-none"
              placeholder="Add a personal message to the invitation..."
            />
          </div>

          <div className="flex justify-end space-x-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={isLoading}
              className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
            >
              {isLoading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Sending...</span>
                </>
              ) : (
                <>
                  <Mail className="w-4 h-4" />
                  <span>Send Invitation</span>
                </>
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
