from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import datetime


class EmployeeCreate(BaseModel):
    """Schema for creating a new employee"""
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

    @validator('employee_id')
    def validate_employee_id(cls, v):
        if not v or len(v) > 20:
            raise ValueError('Employee ID must be 1-20 characters')
        return v

    @validator('full_name')
    def validate_full_name(cls, v):
        if not v or len(v) > 100:
            raise ValueError('Full name must be 1-100 characters')
        return v

    @validator('department')
    def validate_department(cls, v):
        if not v or len(v) > 50:
            raise ValueError('Department must be 1-50 characters')
        return v

    class Config:
        schema_extra = {
            "example": {
                "employee_id": "EMP001",
                "full_name": "John Doe",
                "email": "john.doe@example.com",
                "department": "Engineering"
            }
        }


class EmployeeResponse(BaseModel):
    """Schema for employee response"""
    id: str
    employee_id: str
    full_name: str
    email: str
    department: str
    created_at: datetime

    class Config:
        orm_mode = True


class EmployeeListResponse(BaseModel):
    """Schema for list of employees response"""
    employees: List[EmployeeResponse]
    total: int
