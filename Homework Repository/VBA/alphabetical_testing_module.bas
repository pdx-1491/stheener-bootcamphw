Attribute VB_Name = "Module1"
Sub stock_calc()
    
    'variables
    Dim open_price As Double
    open_price = Cells(2, 3).Value
    
    Dim close_price As Double
    close_price = 0
    
    Dim yearly_change As Double
    yearly_change = 0
    
    Dim total_volume As Double
    total_volume = 0
    
    'table variable
    Dim table_row As Integer
    table_row = 2

    'set column headers
    Cells(1, 9).Value = "Ticker"
    
    Cells(1, 10).Value = "Yearly Change"
    
    Cells(1, 11).Value = "Percent Change"
    
    Cells(1, 12).Value = "Total Stock Volume"
    
    'begin for calculating loop
    For i = 2 To 70926
        
        'start and set the total volume variable calculation
        total_volume = total_volume + Cells(i, 7)
        
            'check Column A until the next value in Column A is different
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            
                'set the close price variable
                close_price = Cells(i, 6).Value
            
                'calculate yearly change variable
                yearly_change = close_price - open_price
                
                'begin populating table_rows
                'populate ticker column (I)
                Cells(table_row, 9).Value = Cells(i, 1).Value
                
                'populate yearly change column (J)
                Cells(table_row, 10).Value = yearly_change
                    
                    'conditional formatting yearly change column
                    If yearly_change > 0 Then
                
                        Cells(table_row, 10).Interior.ColorIndex = 4
                        
                    Else
                        
                        Cells(table_row, 10).Interior.ColorIndex = 3
                        
                    End If
            
                'populate percent change column (K)
                Cells(table_row, 11).Value = ((close_price - open_price) / open_price)
                
                ''format percentage change column (K)
                Cells(table_row, 11).NumberFormat = "0.00%"
                
                'populate total volumen column (L(
                Cells(table_row, 12).Value = total_volume
            
                'iterate the table row so it prints on the next line during the next loop
                table_row = table_row + 1
                
                ''reset variables for next i
                yearly_change = 0
        
                'reset close price variable to 0
                close_price = 0
       
                'reset close price variable to 0
                total_volume = 0
       
                'reset close price variable to 0
                open_price = Cells(i + 2, 3)
        
            End If
    
    Next i
            
End Sub
