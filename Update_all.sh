#! /bin/bash
python3 Create_MD.py --input 1_preprocessing --output Dockerfile_Preprocessing.md
python3 Create_MD.py --input 2_aligner --output Dockerfile_Aligner.md
python3 Create_MD.py --input 3A_variant_calling --output Dockerfile_Variant_Calling.md
python3 Create_MD.py --input 3B_diff_expression --output Dockerfile_Diff_Expression.md
python3 Create_MD.py --input 4A_assembly --output Dockerfile_Assembler.md
python3 Create_MD.py --input XA_general --output Dockerfile_General.md
python3 Create_MD.py --input XB_quality --output Dockerfile_Quality.md
rm Tabla.tsv
python3 Create_Table.py --input 1_preprocessing --output Tabla.tsv
python3 Create_Table.py --input 2_aligner --output Tabla.tsv
python3 Create_Table.py --input 3A_variant_calling --output Tabla.tsv
python3 Create_Table.py --input 3B_diff_expression --output Tabla.tsv
python3 Create_Table.py --input 4A_assembly --output Tabla.tsv
python3 Create_Table.py --input XA_general --output Tabla.tsv
python3 Create_Table.py --input XB_quality --output Tabla.tsv

