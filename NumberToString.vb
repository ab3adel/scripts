Imports System
Imports System.Collections.Generic
Imports System.Text

Public Class NumberToString
    ' Words Arrays   
    Private ahad() As String = {"", "واحد", "إثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", " ثمانية", " تسعة", " عشرة", " أحد", " اثنا"}
    Private ahad2() As String = {"", "واحد", "إثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة", " عشر", " أحد", " اثنا"}
    Private asharat() As String = {"", "واحد", "عشرون", "ثلاثون", "أربعون", "خمسون", "ستون", "سبعون", "ثمانون", "تسعون"}
    Private meat() As String = {"", "مائة", "مائتين", "ثلاثمائة", "أربعمائة", "خمسمائة", "ستمائة", "سبعمائة", "ثمانمائة", "تسعمائة"}
    Private melion() As String = {"", " مليون", " مليونان", " ملايين"}
    Private alf() As String = {"", " ألف", " ألفان", " آلاف"}
    Private bcur() As String = {" ريال سعودي ", " ريال سعودي ", " ريال سعودي "}


    Public Function NumToStr(ByVal P_Numas As Double) As String
        Dim rv As Double
        Dim accum As String = ""

        'Melion
        rv = Math.Floor(P_Numas / 1000000)
        If rv > 2 Then
            accum = NumToStr1(rv, accum)
        End If
        If rv > 2 And rv < 10 Then
            accum += melion(3)
        ElseIf rv = 2 Then
            accum += melion(2)
        ElseIf rv = 1 Or (rv >= 10 And rv <= 999) Then
            accum += melion(1)
        End If

        ' Thousands
        rv = P_Numas - (Math.Floor(P_Numas / 1000000) * 1000000)
        rv = Math.Floor(rv / 1000)
        If P_Numas <> (Math.Floor(P_Numas / 1000000) * 1000000) And P_Numas > 1000000 Then
            accum += " و"
        End If
        If rv > 2 Then
            accum = NumToStr1(rv, accum)
        End If
        If rv > 2 And rv < 10 Then
            accum += alf(3)
        ElseIf rv = 2 Then
            accum += alf(2)
        ElseIf rv = 1 Or (rv >= 10 And rv <= 999) Then
            accum += alf(1)
        End If

        'Rest
        rv = P_Numas - (Math.Floor(P_Numas / 1000) * 1000)
        rv = Math.Floor(rv + 0.0001)

        If P_Numas <> (Math.Floor(P_Numas / 1000) * 1000) And P_Numas > 1000 And rv <> 0 Then
            accum += " و"
        End If
        If rv >= 2 And P_Numas <> 2 Then
            accum = NumToStr1(rv, accum)
        End If
        If P_Numas > 0.999 Then
            If P_Numas < 11 And P_Numas > 2 Then
                accum += bcur(2)
            ElseIf P_Numas = 2 Then
                accum += bcur(1)
            Else
                accum += bcur(0)
            End If
        End If
        Return accum
    End Function
    Public Function NumToStrRational(ByVal P_Numas As Double) As String
        Dim rv As Double
        Dim accum As String = ""

        'Melion
        rv = Math.Floor(P_Numas / 1000000)
        If rv > 2 Then
            accum = NumToStr1(rv, accum)
        End If
        If rv > 2 And rv < 10 Then
            accum += melion(3)
        ElseIf rv = 2 Then
            accum += melion(2)
        ElseIf rv = 1 Or (rv >= 10 And rv <= 999) Then
            accum += melion(1)
        End If

        ' Thousands
        rv = P_Numas - (Math.Floor(P_Numas / 1000000) * 1000000)
        rv = Math.Floor(rv / 1000)
        If P_Numas <> (Math.Floor(P_Numas / 1000000) * 1000000) And P_Numas > 1000000 Then
            accum += " و"
        End If
        If rv > 2 Then
            accum = NumToStr1(rv, accum)
        End If
        If rv > 2 And rv < 10 Then
            accum += alf(3)
        ElseIf rv = 2 Then
            accum += alf(2)
        ElseIf rv = 1 Or (rv >= 10 And rv <= 999) Then
            accum += alf(1)
        End If

        'Rest
        rv = P_Numas - (Math.Floor(P_Numas / 1000) * 1000)
        rv = Math.Floor(rv + 0.0001)

        If P_Numas <> (Math.Floor(P_Numas / 1000) * 1000) And P_Numas > 1000 And rv <> 0 Then
            accum += " و"
        End If
        If rv >= 2 And P_Numas <> 2 Then
            accum = NumToStr1(rv, accum)
        End If
        'If P_Numas > 0.999 Then
        '    If P_Numas < 11 And P_Numas > 2 Then
        '        accum += bcur(2)
        '    ElseIf P_Numas = 2 Then
        '        accum += bcur(1)
        '    Else
        '        accum += bcur(0)
        '    End If
        'End If
        Return accum
    End Function

    Public Function NumToStr1(ByVal rv As Double, ByVal accum As String) As String
        Dim b, c As Integer
        If rv >= 100 Then
            b = Math.Floor(rv / 100)
            accum = accum + meat(b)
        End If

        b = rv - (Math.Floor(rv / 100) * 100)
        If b <> 0 And b > 99 Then
            accum += " و"
        End If

        c = b - (Math.Floor(b / 10) * 10)
        If accum.Length <> 0 And c <> 0 Then
            accum += " و"
        End If
        If b < 13 And b <> 0 Then
            accum += ahad(b)
        End If
        If b > 12 And c <> 0 Then
            accum += ahad2(c)
        End If
        If b > 10 And b < 20 Then
            accum += ahad2(10)
        End If

        If b > 19 Then
            If accum.Length <> 0 Then
                accum += " و"
            End If
            accum += asharat(Math.Floor(b / 10))
        End If

        Return accum
    End Function
End Class
