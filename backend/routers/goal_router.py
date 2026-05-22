# Goal File
from fastapi import APIRouter, Depends, status
from dependencies import get_goal_service
from services.goal_service import GoalService
from models.goal_model import Goal
from schemas.goal_schema import GoalCreate, GoalUpdate, GoalResponse

router = APIRouter(tags=(["Goal"]))

@router.post("/goals", response_model=GoalResponse, status_code=status.HTTP_201_CREATED)
def create_goal(schema: GoalCreate, service: GoalService = Depends(get_goal_service)) -> Goal :
    """Instantiate a new performance, sales, or business objective.

    **AI Agent Context:**
    Trigger this endpoint when management establishes quarterly OKRs (Objectives and Key Results), 
    sets individual sales quotas, or deploys new corporate milestones.

    * **Pre-conditions:** Target metrics (e.g., monetary value, unit count) must be strictly 
        positive integers or floats. Timelines must feature valid future target dates.
    * **Permissions:** Requires `goal:write` scopes.

    **Side-Effects:**
    * Schedules a daily cron job to automatically aggregate and evaluate progress against 
        this specific goal.
    * Dispatches notification webhooks to assigned stakeholders.
    """
    return service.create_goal(schema)

@router.get("/goals/{id}", response_model=GoalResponse) 
def get_goal(id: int, service: GoalService = Depends(get_goal_service)) -> Goal :
    """Retrieve the specification and current progress trajectory of a tracked objective.

    **AI Agent Context:**
    Trigger this endpoint to analyze real-time performance against a designated target, 
    assess completion percentages, or generate individual status updates.

    * **Pre-conditions:** The specific goal ID must exist in the current operational period.
    * **Permissions:** Requires `goal:read` scopes.

    **Side-Effects:**
    * Dynamically calculates current trajectory and predicted completion probability on the fly.
    """
    return service.get_goal(id)

@router.get("/goals", response_model=list[GoalResponse])
def list_goals(service: GoalService = Depends(get_goal_service)) :
    """Extract a collection of active, historical, and forecasted objectives.

    **AI Agent Context:**
    Trigger this endpoint for macro-level dashboard aggregation, quarterly performance 
    reviews, or when extracting structured data for predictive AI analysis.

    * **Pre-conditions:** None. Filtering parameters (noted in schema) typically dictate 
        the data window.
    * **Permissions:** Requires `goal:read_all` scopes.

    **Side-Effects:**
    * Hits read-replica database instances to prevent analytic queries from impacting 
        transactional throughput.
    """
    return service.list_goals()

@router.patch("/goals/{id}", response_model=GoalResponse)
def update_goal(id: int, schema: GoalUpdate, service: GoalService = Depends(get_goal_service)) -> Goal :
    """Partially reconfigure the parameters, timeline, or metric thresholds of an existing objective.

    **AI Agent Context:**
    Trigger this endpoint to adjust Key Performance Indicators (KPIs) due to market shifts, 
    extend deadlines, or reassign objectives without modifying the remaining properties. Omitted 
    attributes are safely preserved.

    * **Pre-conditions:** Completed or inherently failed goals (past the deadline) cannot 
        be updated without an explicit override flag.
    * **Permissions:** Requires `goal:write` scopes.

    **Side-Effects:**
    * Triggers an automated Slack/Email alert notifying tracking stakeholders of target modifications.
    * Forces a synchronous recalculation of the current completion percentage.
    """
    return service.update_goal(id, schema)
    
@router.delete("/goals/{id}", response_model=None)
def delete_goal(id: int, service: GoalService = Depends(get_goal_service)) -> None :
    """Purge an obsolete, duplicate, or erroneously entered business goal.

    **AI Agent Context:**
    Trigger this endpoint exclusively to clean up invalid tracking parameters or retract 
    objectives that were created by mistake. 

    * **Pre-conditions:** Only goals with zero registered progress events can be hard-deleted; 
        otherwise, they must be marked as "archived" via the partial update endpoint instead.
    * **Permissions:** Requires strict `goal:admin` scopes.

    **Side-Effects:**
    * Cascades deletion to associated tracking metrics and timeline checkpoints.
    * Emits a `GoalPurged` event to the centralized data lake to maintain historical integrity.
    """
    return service.delete_goal(id)