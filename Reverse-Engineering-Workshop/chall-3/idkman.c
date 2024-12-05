INT_PTR __stdcall DialogFunc(HWND hWnd, UINT a2, WPARAM a3, LPARAM a4)
{
  HMODULE ModuleHandleA; // eax
  HICON IconA; // eax
  HMODULE v6; // eax
  HICON v7; // eax
  int v9; // esi
  CHAR *lpString; // [esp+18h] [ebp-10h]

  if ( a2 == 272 )
  {
    ModuleHandleA = GetModuleHandleA(0);
    IconA = LoadIconA(ModuleHandleA, (LPCSTR)0x6B);
    SendMessageA(hWnd, 0x80u, 0, (LPARAM)IconA);
    v6 = GetModuleHandleA(0);
    v7 = LoadIconA(v6, (LPCSTR)0x6B);
    SendMessageA(hWnd, 0x80u, 1u, (LPARAM)v7);
    return 1;
  }
  if ( a2 == 273 )
  {
    if ( (unsigned __int16)a3 == 2 )
    {
      EndDialog(hWnd, (unsigned __int16)a3);
      return 1;
    }
    if ( (unsigned __int16)a3 == 1 )
    {
      lpString = (CHAR *)GlobalAlloc(0x40u, 0x64u);
      GetDlgItemTextA(hWnd, 1000, lpString, 90);
      v9 = (unsigned __int16)sub_4036C0(&unk_41A4FC);
      if ( v9 == (unsigned __int16)sub_403A20(lpString, strlen(lpString)) && strlen(lpString) > 0xF )
        SetDlgItemTextA(hWnd, 1001, "Correct!!");
      else
        SetDlgItemTextA(hWnd, 1001, "Wrong");
      GlobalFree(lpString);
    }
  }
  return 0;
}
