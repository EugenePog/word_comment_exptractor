# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:11:28 2023

@author: Eugene
"""

from docx import Document

def get_comments_from_file(file):
    
    document = Document(file)
    paragraphs = document.paragraphs
    
    agg_comments = []
    
    for paragraph in paragraphs:
        comments = paragraph.comments
        for comment in comments:
            x = comment.element.values()
            if x is not None:
                agg_comments.append(x)

    return agg_comments


