#!/usr/bin/python3
"""Difine class LockedClass"""
class LockedClass:
    """
    this class will privent prevents the user from dynamically 
    creating new instance attributes
    """
    __slots__ = ["first_name"]
