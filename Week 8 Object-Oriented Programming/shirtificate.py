# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:26:51 2022

@author: psen
"""

from fpdf import FPDF

name = input("Name: ").strip()

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")