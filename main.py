from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session 

from database import get_db, Base, engine
from models import Issue
from schemas import IssueCreate, IssueUpdate, IssueOut

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Issue Tracker Api")

@app.get("/")
def home():
    return{"message": "Issue Tracker Api Running"}

@app.post("/issue", response_model=IssueOut)
def create_post(issue: IssueCreate, db: Session = Depends(get_db)):
    new_issue = Issue(
       title= issue.title,
       description= issue.description,
       category= issue.category,
       priority= issue.priority,
       status= "Open"
    )
    
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    
    return new_issue

@app.get("/issues", response_model=list[IssueOut])
def get_issues(db: Session = Depends(get_db)):
    Issues= db.query(Issue).all()
    return Issues

@app.get("/issues/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = db.query(Issue). filter(Issue.id==issue_id).first()
    
    if not issue:
        raise HTTPException(status_code=404, detail="Issue Not Found")
    return issue 

@app.put("/issue/{issue_id}", response_model=IssueOut)
def update_issue(issue_id:int, issue_data:IssueUpdate, db:Session = Depends(get_db)):
    issue = db.query(Issue).filter(Issue.id==issue_id).first()
    
    if not issue:
        raise HTTPException(status_code=404, detail="Issue Not Found")
    
    if issue_data.title is not None:
        issue.title= issue_data.title
        
    if issue_data.description is not None:
        issue.description= issue_data.description
    
    if issue_data.category is not None:
        issue.category= issue_data.category
    
    if issue_data.priority is not None:
        issue.priority= issue_data.priority
    
    if issue_data.status is not None:
        issue.status= issue_data.status
        
    db.commit() 
    db.refresh(issue)
    
    return issue 

@app.delete("/issues/{issue_id}")
def delete_issue(issue_id: int, db:Session = Depends(get_db)):
    issue = db.query(Issue).filter(Issue.id==issue_id).first()
 
    if not issue:
        raise HTTPException(status_code=404, detail="Issue Not Found")
    
    db.delete(issue)
    db.commit()
    
    return{"message": "Issue delete Successfully"}


@app.get("/issue/status/{status}", response_model=list[IssueOut])
def get_issue_by_status(status: str, db:Session = Depends(get_db)):
    issues = db.query(Issue).filter(Issue.status==status).all()
    return issues

@app.get("/issue/priority/{priority}", response_model=list[IssueOut])
def get_issue_by_priority(priority: str, db:Session = Depends(get_db)):
    issues = db.query(Issue).filter(Issue.priority==priority).all()
    return issues 