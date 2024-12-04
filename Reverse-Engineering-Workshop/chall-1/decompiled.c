INT_PTR __stdcall DialogFunc(HWND hDlg, UINT a2, WPARAM a3, LPARAM a4)
{
  char v4; // ah
  unsigned int v5; // edi
  unsigned int v6; // kr00_4
  char v7; // dl
  HMODULE ModuleHandleA; // eax
  HICON IconA; // eax
  HMODULE v11; // eax
  HICON v12; // eax
  char String[100]; // [esp+10h] [ebp-68h] BYREF
  int v14; // [esp+74h] [ebp-4h]
  int savedregs; // [esp+78h] [ebp+0h] BYREF

  if ( a2 == 272 )
  {
    ModuleHandleA = GetModuleHandleA(0);
    IconA = LoadIconA(ModuleHandleA, (LPCSTR)0x6B);
    SendMessageA(hDlg, 0x80u, 0, (LPARAM)IconA);
    v11 = GetModuleHandleA(0);
    v12 = LoadIconA(v11, (LPCSTR)0x6B);
    SendMessageA(hDlg, 0x80u, 1u, (LPARAM)v12);
    return nullsub_1((unsigned int)&savedregs ^ v14, hDlg);
  }
  if ( a2 != 273 )
    return nullsub_1((unsigned int)&savedregs ^ v14, hDlg);
  if ( (unsigned __int16)a3 != 2 )
  {
    if ( (unsigned __int16)a3 == 1 )
    {
      sub_4010FA(String, 0, 0x64u);
      GetDlgItemTextA(hDlg, 1000, String, 90);
      v4 = 1;
      v5 = 0;
      v6 = strlen(String);
      if ( v6 )
      {
        do
        {
          v7 = 0;
          if ( ((unsigned __int8)String[v5] ^ 0x65) == byte_402050[v5] )
            v7 = v4;
          ++v5;
          v4 = v7;
        }
        while ( v5 < v6 );
        if ( v7 == 1 && v5 == 20 )
        {
          SetDlgItemTextA(hDlg, 1001, "Correct!!");
          return nullsub_1((unsigned int)&savedregs ^ v14, hDlg);
        }
      }
      SetDlgItemTextA(hDlg, 1001, "Wrong!!");
    }
    return nullsub_1((unsigned int)&savedregs ^ v14, hDlg);
  }
  EndDialog(hDlg, 2);
  return nullsub_1((unsigned int)&savedregs ^ v14, hDlg);
}
