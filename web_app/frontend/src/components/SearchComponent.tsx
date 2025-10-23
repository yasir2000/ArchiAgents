import { useState, useEffect } from 'react';
import { Search, X, Filter, Calendar, Tag, FileBox, Loader2 } from 'lucide-react';
import { apiClient } from '../lib/api-client';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-hot-toast';

interface SearchComponentProps {
  isOpen: boolean;
  onClose: () => void;
}

interface SearchResult {
  id: string;
  name: string;
  type: string;
  description: string;
  project_id: string;
  project_name: string;
  status: string;
  created_at: string;
  updated_at: string;
}

const MODEL_TYPE_FILTERS = [
  'All Types',
  'ArchiMate - Business',
  'ArchiMate - Application',
  'ArchiMate - Technology',
  'ArchiMate - Strategy',
  'ArchiMate - Physical',
  'BPMN - Process',
  'BPMN - Collaboration',
  'UML - Class',
  'UML - Sequence',
  'UML - Activity',
];

const STATUS_FILTERS = ['All Status', 'draft', 'in_review', 'approved', 'published'];

const DATE_FILTERS = [
  { label: 'Any Time', value: 'all' },
  { label: 'Last 24 Hours', value: '1d' },
  { label: 'Last 7 Days', value: '7d' },
  { label: 'Last 30 Days', value: '30d' },
  { label: 'Last 90 Days', value: '90d' },
];

export default function SearchComponent({ isOpen, onClose }: SearchComponentProps) {
  const navigate = useNavigate();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [showFilters, setShowFilters] = useState(false);

  const [filters, setFilters] = useState({
    modelType: 'All Types',
    status: 'All Status',
    dateRange: 'all',
    tags: [] as string[],
  });

  // Debounced search
  useEffect(() => {
    if (query.length < 2) {
      setResults([]);
      return;
    }

    const timer = setTimeout(() => {
      performSearch();
    }, 300);

    return () => clearTimeout(timer);
  }, [query]);

  const performSearch = async () => {
    setIsLoading(true);
    try {
      const params = new URLSearchParams();
      params.append('q', query);

      if (filters.modelType !== 'All Types') {
        params.append('model_type', filters.modelType);
      }
      if (filters.status !== 'All Status') {
        params.append('status', filters.status);
      }
      if (filters.dateRange !== 'all') {
        params.append('date_range', filters.dateRange);
      }

      const response = await apiClient.get(`/search?${params.toString()}`);
      setResults(response.data.results || []);
    } catch (error: any) {
      toast.error('Search failed');
      console.error('Search error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleResultClick = (result: SearchResult) => {
    navigate(`/models/${result.id}`);
    onClose();
  };

  const clearFilters = () => {
    setFilters({
      modelType: 'All Types',
      status: 'All Status',
      dateRange: 'all',
      tags: [],
    });
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-start justify-center z-50 pt-20 px-4">
      <div className="bg-white rounded-lg shadow-2xl max-w-4xl w-full max-h-[80vh] flex flex-col">
        {/* Header */}
        <div className="p-4 border-b border-gray-200">
          <div className="flex items-center space-x-3">
            <Search className="w-6 h-6 text-gray-400" />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search models, projects, descriptions..."
              className="flex-1 text-lg outline-none"
              autoFocus
            />
            <button
              onClick={() => setShowFilters(!showFilters)}
              className={`p-2 rounded-lg transition-colors ${
                showFilters ? 'bg-blue-100 text-blue-600' : 'text-gray-400 hover:bg-gray-100'
              }`}
            >
              <Filter className="w-5 h-5" />
            </button>
            <button
              onClick={onClose}
              className="p-2 text-gray-400 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Filters Panel */}
          {showFilters && (
            <div className="mt-4 p-4 bg-gray-50 rounded-lg space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {/* Model Type Filter */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Model Type
                  </label>
                  <select
                    value={filters.modelType}
                    onChange={(e) => setFilters({ ...filters, modelType: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
                  >
                    {MODEL_TYPE_FILTERS.map((type) => (
                      <option key={type} value={type}>
                        {type}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Status Filter */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Status
                  </label>
                  <select
                    value={filters.status}
                    onChange={(e) => setFilters({ ...filters, status: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
                  >
                    {STATUS_FILTERS.map((status) => (
                      <option key={status} value={status}>
                        {status}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Date Range Filter */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Date Range
                  </label>
                  <select
                    value={filters.dateRange}
                    onChange={(e) => setFilters({ ...filters, dateRange: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
                  >
                    {DATE_FILTERS.map((date) => (
                      <option key={date.value} value={date.value}>
                        {date.label}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Clear Filters */}
              <div className="flex justify-end">
                <button
                  onClick={clearFilters}
                  className="text-sm text-blue-600 hover:text-blue-700 font-medium"
                >
                  Clear all filters
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Results */}
        <div className="flex-1 overflow-y-auto p-4">
          {isLoading && (
            <div className="flex items-center justify-center py-12">
              <Loader2 className="w-8 h-8 text-blue-600 animate-spin" />
            </div>
          )}

          {!isLoading && query.length < 2 && (
            <div className="text-center py-12">
              <Search className="w-16 h-16 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500">Type at least 2 characters to search</p>
              <p className="text-sm text-gray-400 mt-2">
                Search across models, projects, and descriptions
              </p>
            </div>
          )}

          {!isLoading && query.length >= 2 && results.length === 0 && (
            <div className="text-center py-12">
              <Search className="w-16 h-16 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500">No results found for "{query}"</p>
              <p className="text-sm text-gray-400 mt-2">
                Try different keywords or adjust your filters
              </p>
            </div>
          )}

          {!isLoading && results.length > 0 && (
            <div className="space-y-3">
              <p className="text-sm text-gray-600 mb-4">
                Found {results.length} result{results.length !== 1 ? 's' : ''}
              </p>

              {results.map((result) => (
                <button
                  key={result.id}
                  onClick={() => handleResultClick(result)}
                  className="w-full text-left p-4 bg-white border border-gray-200 rounded-lg hover:border-blue-500 hover:shadow-md transition-all"
                >
                  <div className="flex items-start justify-between">
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center space-x-2 mb-2">
                        <FileBox className="w-4 h-4 text-gray-400 flex-shrink-0" />
                        <h3 className="font-semibold text-gray-900 truncate">
                          {result.name}
                        </h3>
                        <span
                          className={`px-2 py-0.5 text-xs rounded-full ${
                            result.status === 'published'
                              ? 'bg-blue-100 text-blue-700'
                              : result.status === 'approved'
                              ? 'bg-green-100 text-green-700'
                              : result.status === 'in_review'
                              ? 'bg-yellow-100 text-yellow-700'
                              : 'bg-gray-100 text-gray-700'
                          }`}
                        >
                          {result.status}
                        </span>
                      </div>

                      {result.description && (
                        <p className="text-sm text-gray-600 mb-2 line-clamp-2">
                          {result.description}
                        </p>
                      )}

                      <div className="flex items-center space-x-4 text-xs text-gray-500">
                        <span className="flex items-center space-x-1">
                          <Tag className="w-3 h-3" />
                          <span>{result.type}</span>
                        </span>
                        <span className="flex items-center space-x-1">
                          <FileBox className="w-3 h-3" />
                          <span>{result.project_name}</span>
                        </span>
                        <span className="flex items-center space-x-1">
                          <Calendar className="w-3 h-3" />
                          <span>
                            Updated {new Date(result.updated_at).toLocaleDateString()}
                          </span>
                        </span>
                      </div>
                    </div>
                  </div>
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Footer with keyboard shortcuts */}
        <div className="p-3 border-t border-gray-200 bg-gray-50 text-xs text-gray-500 flex items-center justify-between rounded-b-lg">
          <div className="flex items-center space-x-4">
            <span>
              <kbd className="px-2 py-1 bg-white border border-gray-300 rounded">↑</kbd>
              <kbd className="px-2 py-1 bg-white border border-gray-300 rounded ml-1">↓</kbd>
              <span className="ml-2">Navigate</span>
            </span>
            <span>
              <kbd className="px-2 py-1 bg-white border border-gray-300 rounded">Enter</kbd>
              <span className="ml-2">Open</span>
            </span>
            <span>
              <kbd className="px-2 py-1 bg-white border border-gray-300 rounded">Esc</kbd>
              <span className="ml-2">Close</span>
            </span>
          </div>
          <span>{results.length} results</span>
        </div>
      </div>
    </div>
  );
}
