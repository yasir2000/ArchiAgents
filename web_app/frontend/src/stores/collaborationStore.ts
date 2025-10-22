import { create } from 'zustand'
import type { CollaborationUpdate } from '../types'

interface Participant {
  user_id: number
  username: string
  cursor?: { x: number; y: number }
  color: string
}

interface CollaborationState {
  ws: WebSocket | null
  isConnected: boolean
  participants: Participant[]
  sessionToken: string | null
  connect: (token: string, userId: number) => void
  disconnect: () => void
  sendUpdate: (update: CollaborationUpdate) => void
  onUpdate: ((update: CollaborationUpdate) => void) | null
  setOnUpdate: (callback: (update: CollaborationUpdate) => void) => void
}

const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']

export const useCollaborationStore = create<CollaborationState>((set, get) => ({
  ws: null,
  isConnected: false,
  participants: [],
  sessionToken: null,
  onUpdate: null,

  connect: (token, userId) => {
    const wsUrl = `${window.location.protocol === 'https:' ? 'wss:' : 'ws:'}//${window.location.host}/ws/collaboration/${token}`
    const ws = new WebSocket(wsUrl)

    ws.onopen = () => {
      console.log('WebSocket connected')
      set({ isConnected: true, sessionToken: token })
    }

    ws.onmessage = (event) => {
      const update: CollaborationUpdate = JSON.parse(event.data)
      console.log('Received update:', update)

      // Handle presence updates
      if (update.type === 'user_joined' && update.data.user_id) {
        set((state) => ({
          participants: [
            ...state.participants,
            {
              user_id: update.data.user_id,
              username: update.data.username,
              color: colors[state.participants.length % colors.length],
            },
          ],
        }))
      } else if (update.type === 'user_left') {
        set((state) => ({
          participants: state.participants.filter((p) => p.user_id !== update.data.user_id),
        }))
      } else if (update.type === 'cursor_move') {
        set((state) => ({
          participants: state.participants.map((p) =>
            p.user_id === update.user_id
              ? { ...p, cursor: update.data }
              : p
          ),
        }))
      }

      // Call the update callback
      const { onUpdate } = get()
      if (onUpdate) {
        onUpdate(update)
      }
    }

    ws.onerror = (error) => {
      console.error('WebSocket error:', error)
    }

    ws.onclose = () => {
      console.log('WebSocket disconnected')
      set({ isConnected: false, ws: null, participants: [] })
    }

    set({ ws })
  },

  disconnect: () => {
    const { ws } = get()
    if (ws) {
      ws.close()
    }
    set({ ws: null, isConnected: false, participants: [], sessionToken: null })
  },

  sendUpdate: (update) => {
    const { ws, isConnected } = get()
    if (ws && isConnected) {
      ws.send(JSON.stringify(update))
    }
  },

  setOnUpdate: (callback) => {
    set({ onUpdate: callback })
  },
}))
