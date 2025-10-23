import { useState, useEffect } from 'react';
import { User, Lock, Bell, Palette, Save, Loader2, CheckCircle, AlertCircle } from 'lucide-react';
import { apiClient } from '../lib/api-client';
import { useAuthStore } from '../stores/authStore';
import { toast } from 'react-hot-toast';

interface UserProfile {
  id: string;
  email: string;
  username: string;
  full_name: string;
  role: string;
  created_at: string;
}

export default function SettingsPage() {
  const { user, fetchCurrentUser } = useAuthStore();
  const [activeTab, setActiveTab] = useState<'profile' | 'security' | 'preferences'>('profile');
  const [isLoading, setIsLoading] = useState(false);
  const [success, setSuccess] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  // Profile form
  const [profileData, setProfileData] = useState({
    email: '',
    full_name: '',
    username: '',
  });

  // Password form
  const [passwordData, setPasswordData] = useState({
    current_password: '',
    new_password: '',
    confirm_password: '',
  });

  // Preferences
  const [preferences, setPreferences] = useState({
    emailNotifications: true,
    projectNotifications: true,
    collaborationNotifications: true,
    theme: 'light',
    language: 'en',
    timezone: 'UTC',
  });

  useEffect(() => {
    if (user) {
      setProfileData({
        email: user.email,
        full_name: user.full_name,
        username: user.username,
      });
    }
  }, [user]);

  const handleUpdateProfile = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);
    setIsLoading(true);

    try {
      await apiClient.put('/auth/me', profileData);
      await fetchCurrentUser();
      setSuccess('Profile updated successfully!');
      toast.success('Profile updated!');
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to update profile';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  const handleUpdatePassword = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    if (passwordData.new_password !== passwordData.confirm_password) {
      setError('New passwords do not match');
      return;
    }

    if (passwordData.new_password.length < 8) {
      setError('Password must be at least 8 characters long');
      return;
    }

    setIsLoading(true);

    try {
      await apiClient.post('/auth/change-password', {
        current_password: passwordData.current_password,
        new_password: passwordData.new_password,
      });

      setSuccess('Password updated successfully!');
      toast.success('Password updated!');
      setPasswordData({
        current_password: '',
        new_password: '',
        confirm_password: '',
      });
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to update password';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  const handleUpdatePreferences = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);
    setIsLoading(true);

    try {
      // Store preferences in localStorage for now (backend endpoint can be added later)
      localStorage.setItem('user_preferences', JSON.stringify(preferences));
      setSuccess('Preferences updated successfully!');
      toast.success('Preferences updated!');
    } catch (err: any) {
      const errorMessage = 'Failed to update preferences';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  const tabs = [
    { id: 'profile', label: 'Profile', icon: User },
    { id: 'security', label: 'Security', icon: Lock },
    { id: 'preferences', label: 'Preferences', icon: Bell },
  ];

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Settings</h1>
        <p className="text-gray-600 mt-2">Manage your account settings and preferences</p>
      </div>

      {/* Tabs */}
      <div className="border-b border-gray-200">
        <nav className="flex space-x-8">
          {tabs.map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;

            return (
              <button
                key={tab.id}
                onClick={() => {
                  setActiveTab(tab.id as any);
                  setError(null);
                  setSuccess(null);
                }}
                className={`flex items-center space-x-2 py-4 px-1 border-b-2 font-medium text-sm transition-colors ${
                  isActive
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <Icon className="w-5 h-5" />
                <span>{tab.label}</span>
              </button>
            );
          })}
        </nav>
      </div>

      {/* Alerts */}
      {success && (
        <div className="bg-green-50 border border-green-200 rounded-lg p-4 flex items-start space-x-3">
          <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
          <p className="text-sm text-green-800">{success}</p>
        </div>
      )}

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-3">
          <AlertCircle className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" />
          <p className="text-sm text-red-800">{error}</p>
        </div>
      )}

      {/* Profile Tab */}
      {activeTab === 'profile' && (
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-6">Profile Information</h2>
          <form onSubmit={handleUpdateProfile} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Email Address
              </label>
              <input
                type="email"
                value={profileData.email}
                onChange={(e) => setProfileData({ ...profileData, email: e.target.value })}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Username
              </label>
              <input
                type="text"
                value={profileData.username}
                onChange={(e) => setProfileData({ ...profileData, username: e.target.value })}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Full Name
              </label>
              <input
                type="text"
                value={profileData.full_name}
                onChange={(e) => setProfileData({ ...profileData, full_name: e.target.value })}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Role</label>
              <input
                type="text"
                value={user?.role || 'viewer'}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-600"
                disabled
              />
              <p className="text-xs text-gray-500 mt-1">
                Contact an administrator to change your role
              </p>
            </div>

            <div className="flex justify-end">
              <button
                type="submit"
                disabled={isLoading}
                className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
              >
                {isLoading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Saving...</span>
                  </>
                ) : (
                  <>
                    <Save className="w-4 h-4" />
                    <span>Save Changes</span>
                  </>
                )}
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Security Tab */}
      {activeTab === 'security' && (
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-6">Change Password</h2>
          <form onSubmit={handleUpdatePassword} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Current Password
              </label>
              <input
                type="password"
                value={passwordData.current_password}
                onChange={(e) =>
                  setPasswordData({ ...passwordData, current_password: e.target.value })
                }
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                New Password
              </label>
              <input
                type="password"
                value={passwordData.new_password}
                onChange={(e) =>
                  setPasswordData({ ...passwordData, new_password: e.target.value })
                }
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
                minLength={8}
              />
              <p className="text-xs text-gray-500 mt-1">
                Must be at least 8 characters long
              </p>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Confirm New Password
              </label>
              <input
                type="password"
                value={passwordData.confirm_password}
                onChange={(e) =>
                  setPasswordData({ ...passwordData, confirm_password: e.target.value })
                }
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>

            <div className="flex justify-end">
              <button
                type="submit"
                disabled={isLoading}
                className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
              >
                {isLoading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Updating...</span>
                  </>
                ) : (
                  <>
                    <Lock className="w-4 h-4" />
                    <span>Update Password</span>
                  </>
                )}
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Preferences Tab */}
      {activeTab === 'preferences' && (
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-6">Preferences</h2>
          <form onSubmit={handleUpdatePreferences} className="space-y-8">
            {/* Notifications */}
            <div>
              <h3 className="text-lg font-medium text-gray-900 mb-4">Notifications</h3>
              <div className="space-y-4">
                <label className="flex items-center justify-between">
                  <div>
                    <p className="font-medium text-gray-900">Email Notifications</p>
                    <p className="text-sm text-gray-600">
                      Receive email notifications for important updates
                    </p>
                  </div>
                  <input
                    type="checkbox"
                    checked={preferences.emailNotifications}
                    onChange={(e) =>
                      setPreferences({ ...preferences, emailNotifications: e.target.checked })
                    }
                    className="w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
                  />
                </label>

                <label className="flex items-center justify-between">
                  <div>
                    <p className="font-medium text-gray-900">Project Notifications</p>
                    <p className="text-sm text-gray-600">
                      Get notified about project updates and changes
                    </p>
                  </div>
                  <input
                    type="checkbox"
                    checked={preferences.projectNotifications}
                    onChange={(e) =>
                      setPreferences({ ...preferences, projectNotifications: e.target.checked })
                    }
                    className="w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
                  />
                </label>

                <label className="flex items-center justify-between">
                  <div>
                    <p className="font-medium text-gray-900">Collaboration Notifications</p>
                    <p className="text-sm text-gray-600">
                      Receive alerts when someone mentions you or comments
                    </p>
                  </div>
                  <input
                    type="checkbox"
                    checked={preferences.collaborationNotifications}
                    onChange={(e) =>
                      setPreferences({
                        ...preferences,
                        collaborationNotifications: e.target.checked,
                      })
                    }
                    className="w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
                  />
                </label>
              </div>
            </div>

            {/* Appearance */}
            <div>
              <h3 className="text-lg font-medium text-gray-900 mb-4">Appearance</h3>
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Theme</label>
                  <select
                    value={preferences.theme}
                    onChange={(e) => setPreferences({ ...preferences, theme: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="light">Light</option>
                    <option value="dark">Dark (Coming Soon)</option>
                    <option value="auto">Auto (Coming Soon)</option>
                  </select>
                </div>
              </div>
            </div>

            {/* Regional */}
            <div>
              <h3 className="text-lg font-medium text-gray-900 mb-4">Regional Settings</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Language
                  </label>
                  <select
                    value={preferences.language}
                    onChange={(e) => setPreferences({ ...preferences, language: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="en">English</option>
                    <option value="ar">Arabic (Coming Soon)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Timezone
                  </label>
                  <select
                    value={preferences.timezone}
                    onChange={(e) => setPreferences({ ...preferences, timezone: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="UTC">UTC</option>
                    <option value="America/New_York">Eastern Time</option>
                    <option value="Europe/London">London</option>
                    <option value="Asia/Riyadh">Riyadh</option>
                    <option value="Asia/Dubai">Dubai</option>
                  </select>
                </div>
              </div>
            </div>

            <div className="flex justify-end">
              <button
                type="submit"
                disabled={isLoading}
                className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
              >
                {isLoading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Saving...</span>
                  </>
                ) : (
                  <>
                    <Save className="w-4 h-4" />
                    <span>Save Preferences</span>
                  </>
                )}
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
}
