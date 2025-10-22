import { useEffect, useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { BarChart3, FolderKanban, Users, CheckCircle2 } from 'lucide-react';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip, BarChart, Bar, XAxis, YAxis, CartesianGrid } from 'recharts';
import { apiClient } from '@/lib/api-client';
import { DashboardStats, ActivityLog } from '@/types';

export default function DashboardPage() {
  // Fetch dashboard statistics
  const { data: stats, isLoading: statsLoading } = useQuery<DashboardStats>({
    queryKey: ['dashboard', 'stats'],
    queryFn: async () => {
      const response = await apiClient.get('/dashboard/stats');
      return response.data;
    },
  });

  // Fetch recent activity
  const { data: activities, isLoading: activitiesLoading } = useQuery<ActivityLog[]>({
    queryKey: ['dashboard', 'activity'],
    queryFn: async () => {
      const response = await apiClient.get('/dashboard/activity');
      return response.data;
    },
  });

  // Prepare data for charts
  const modelsByType = stats?.models_by_type || [];
  const modelsByStatus = stats?.models_by_status || [];

  // Colors for pie chart
  const COLORS = ['#3b82f6', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981', '#6366f1', '#14b8a6'];

  // Colors for bar chart
  const STATUS_COLORS: Record<string, string> = {
    draft: '#94a3b8',
    in_review: '#fbbf24',
    approved: '#10b981',
    published: '#3b82f6',
    archived: '#6b7280',
  };

  if (statsLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-gray-600">Loading dashboard...</div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600 mt-1">Overview of your enterprise architecture projects</p>
      </div>

      {/* Statistics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {/* Total Projects */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Total Projects</p>
              <p className="text-3xl font-bold text-gray-900 mt-2">{stats?.total_projects || 0}</p>
            </div>
            <div className="bg-blue-100 rounded-full p-3">
              <FolderKanban className="w-6 h-6 text-blue-600" />
            </div>
          </div>
        </div>

        {/* Total Models */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Total Models</p>
              <p className="text-3xl font-bold text-gray-900 mt-2">{stats?.total_models || 0}</p>
            </div>
            <div className="bg-purple-100 rounded-full p-3">
              <BarChart3 className="w-6 h-6 text-purple-600" />
            </div>
          </div>
        </div>

        {/* Team Members */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Team Members</p>
              <p className="text-3xl font-bold text-gray-900 mt-2">{stats?.team_members || 0}</p>
            </div>
            <div className="bg-green-100 rounded-full p-3">
              <Users className="w-6 h-6 text-green-600" />
            </div>
          </div>
        </div>

        {/* Avg Compliance */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Avg Compliance</p>
              <p className="text-3xl font-bold text-gray-900 mt-2">
                {stats?.avg_compliance_score ? `${stats.avg_compliance_score}%` : 'N/A'}
              </p>
            </div>
            <div className="bg-indigo-100 rounded-full p-3">
              <CheckCircle2 className="w-6 h-6 text-indigo-600" />
            </div>
          </div>
        </div>
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Models by Type - Pie Chart */}
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Models by Type</h2>
          {modelsByType.length > 0 ? (
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={modelsByType}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="count"
                  nameKey="type"
                >
                  {modelsByType.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend />
              </PieChart>
            </ResponsiveContainer>
          ) : (
            <div className="flex items-center justify-center h-[300px] text-gray-500">
              No models available
            </div>
          )}
        </div>

        {/* Models by Status - Bar Chart */}
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Models by Status</h2>
          {modelsByStatus.length > 0 ? (
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={modelsByStatus}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="status" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count" radius={[8, 8, 0, 0]}>
                  {modelsByStatus.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={STATUS_COLORS[entry.status] || '#94a3b8'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          ) : (
            <div className="flex items-center justify-center h-[300px] text-gray-500">
              No models available
            </div>
          )}
        </div>
      </div>

      {/* Recent Activity */}
      <div className="bg-white rounded-lg shadow">
        <div className="p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Recent Activity</h2>
          {activitiesLoading ? (
            <div className="text-center py-8 text-gray-500">Loading activity...</div>
          ) : activities && activities.length > 0 ? (
            <div className="space-y-4">
              {activities.map((activity) => (
                <div key={activity.id} className="flex items-start space-x-3 pb-4 border-b last:border-b-0">
                  <div className="flex-shrink-0 mt-1">
                    <div className="w-2 h-2 bg-blue-600 rounded-full"></div>
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm text-gray-900">
                      <span className="font-medium">{activity.user_name}</span> {activity.action}
                    </p>
                    <p className="text-sm text-gray-600 mt-1">{activity.entity_type}: {activity.entity_name}</p>
                    <p className="text-xs text-gray-500 mt-1">
                      {new Date(activity.created_at).toLocaleString()}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8 text-gray-500">No recent activity</div>
          )}
        </div>
      </div>
    </div>
  );
}
