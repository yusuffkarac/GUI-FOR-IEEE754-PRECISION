import flet as ft
from ieee754 import *

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.DARK
    t = ft.Text()
    def set_predifined_precision(e):
        if e.control.value == "Half Precision":
            exponentSlider.value=5
            mantissaSlider.value=10
            exponent_changed(e)
            mantissa_changed(e)
            page.update()

        elif e.control.value == "Single Precision":
            exponentSlider.value=8
            mantissaSlider.value=23
            exponent_changed(e)
            mantissa_changed(e)
            page.update()
        elif e.control.value == "Double Precision":
            exponentSlider.value=11
            mantissaSlider.value=52
            exponent_changed(e)
            mantissa_changed(e)
            page.update()

        elif e.control.value == "Quadruple Precision":
            exponentSlider.value=15
            mantissaSlider.value=112
            exponent_changed(e)
            mantissa_changed(e)
            page.update()

        elif e.control.value == "Octuple Precision":
            exponentSlider.value=19
            mantissaSlider.value=236
            exponent_changed(e)
            mantissa_changed(e)
            page.update()

    
    binary_sign = ft.Text(weight=ft.FontWeight.W_900,size=22,color=ft.colors.CYAN)
    binary_exponent=ft.Text(weight=ft.FontWeight.W_900,size=22,color=ft.colors.RED)
    binary_mantissa=ft.Text(weight=ft.FontWeight.W_900,size=22,color=ft.colors.BLUE,overflow=ft.TextOverflow.ELLIPSIS)
    bst = ft.Text(value="Sign bit: ",weight=ft.FontWeight.W_900,size=22,color=ft.colors.CYAN)
    
    hex_result=ft.Text(weight=ft.FontWeight.W_900,size=30)
    def button_clicked(e):
        page.window_full_screen = True
        page.auto_scroll = True
        page.update()
        
        def calculate_bias(exp):
            return 2**(exp-1)-1
        float_number = float(intpart.value + "." + decpart.value)
        
        result = IEEE754(float_number,
                    force_length=int(mantissaSlider.value+exponentSlider.value+1),
                    force_exponent=int(exponentSlider.value),
                    force_mantissa=int(mantissaSlider.value),
                    force_bias=calculate_bias(int(exponentSlider.value)))
        hex_result_ = result.str2hex().upper()
        result = str(result)
        binary_sign.value=result[0]
        binary_exponent.value = result[1:int(exponentSlider.value)+1]
        binary_mantissa.value = result[int(exponentSlider.value)+1:]
        bst.value=result
        hex_result.value = hex_result_
        page.update()

        
    convertButton= ft.ElevatedButton(text="Convert", on_click=button_clicked)
    predefinedDropdown = ft.Dropdown(
        width=500,
        hint_text="Select a predefined precision",
        options=[
            ft.dropdown.Option("Half Precision"),
            ft.dropdown.Option("Single Precision"),
            ft.dropdown.Option("Double Precision"),
            ft.dropdown.Option("Quadruple Precision"),
            ft.dropdown.Option("Octuple Precision"),
        ],
        on_change=set_predifined_precision,
    )
    def exponent_changed(e):
        exponentSlider.value = int(exponentSlider.value)
        value_exponent.value = f"Exponent bit: {exponentSlider.value}"
        total_bits.value = (f"Total bits: {int(exponentSlider.value) + int(mantissaSlider.value) + 1}")

        page.update()

    def mantissa_changed(e):
        mantissaSlider.value = int(mantissaSlider.value)
        value_mantissa.value = f"Mantissa bit: {mantissaSlider.value}"
        total_bits.value = (f"Total bits: {int(exponentSlider.value) + int(mantissaSlider.value) + 1}")

        page.update()


    mantissaSlider =ft.Slider(min=0, max=236, divisions=236, label="{value}bits",on_change=mantissa_changed)
    exponentSlider =ft.Slider(min=0, max=19, divisions=19, label="{value} bits",on_change=exponent_changed)

        
    value_sign= ft.Text(f"Sign bit: 1")
    value_exponent= ft.Text()
    value_mantissa= ft.Text()
    total_bits = ft.Text()

    intpart = ft.TextField(hint_text="Integer part")
    dot = ft.Text(".",size=50)
    decpart = ft.TextField(hint_text="Decimal part")
    floatRow = ft.Row([intpart,dot,decpart])

    binary_result_row = ft.Row(
    
                
                width=page.width,
                controls=[
                   binary_sign,binary_exponent,binary_mantissa
                ]
                )

            
    header = ft.Text("IEEE 754 Converter",size=50,weight=ft.FontWeight.W_900)
    page.add(header,predefinedDropdown,exponentSlider,mantissaSlider,value_sign,value_exponent,value_mantissa,total_bits,floatRow,convertButton,binary_result_row,hex_result)

ft.app(target=main)