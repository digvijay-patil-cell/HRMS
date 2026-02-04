from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import date


class AttendanceCreate(BaseModel):
    """Schema for marking attendance"""
    employee_id: str
    date: date
    status: str

    @validator('status')
    def validate_status(cls, v):
        if v not in ['Present', 'Absent']:
            raise ValueError('Status must be either "Present" or "Absent"')
        return v

    class Config:
        schema_extra = {
            "example": {
                "employee_id": "EMP001",
                "date": "2026-02-04",
                "status": "Present"
            }
        }


class AttendanceResponse(BaseModel):
    """Schema for attendance response"""
    id: str
    employee_id: str
    employee_name: str
    date: date
    status: str

    class Config:
        orm_mode = True


class AttendanceListResponse(BaseModel):
    """Schema for list of attendance records"""
    records: List[AttendanceResponse]
    total: int
