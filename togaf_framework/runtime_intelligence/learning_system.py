"""
Architecture Learning System

Learns from architecture decisions and continuously improves recommendations.
"""

from dataclasses import dataclass
from typing import Dict, List, Any
from datetime import datetime


@dataclass
class LearningFeedback:
    """Feedback on architecture decision or recommendation"""
    
    feedback_id: str
    target_id: str  # Decision or recommendation ID
    feedback_type: str  # success, failure, partial_success
    rating: float  # 0-1
    comments: str
    timestamp: datetime


class ArchitectureLearningSystem:
    """Learning system for continuous improvement"""
    
    def __init__(self):
        self.feedback: List[LearningFeedback] = []
        self.patterns: Dict[str, Any] = {}
    
    def record_feedback(self, feedback: LearningFeedback):
        """Record feedback"""
        self.feedback.append(feedback)
    
    def analyze_patterns(self) -> Dict[str, Any]:
        """Analyze patterns from feedback"""
        
        if not self.feedback:
            return {"pattern_count": 0}
        
        # Simple analysis
        success_rate = len([f for f in self.feedback if f.feedback_type == "success"]) / len(self.feedback)
        
        return {
            "pattern_count": len(self.patterns),
            "success_rate": success_rate,
            "total_feedback": len(self.feedback)
        }
