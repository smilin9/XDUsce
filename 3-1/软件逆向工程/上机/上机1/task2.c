// created by: smilin9
// time: 2022-11-26 18:46:16
#include <process.h>
#include <stdio.h>
#include <string.h>
#include <strsafe.h>
#include <tchar.h>
#include <windows.h>

HANDLE handle;

DWORD WINAPI ThreadFun(LPVOID pM)
{
    int sub_id;
    char ker_path[100];
    char sub_id_char[20];
    LPTSTR szKernel32 = TEXT("kernel32.dll");

    // sub_id = GetCurrentThreadId(); //子线程的线程ID
    typedef long long int(WINAPI * PGETID)();
    PGETID GetCurrentThreadId_addrs;

    HMODULE h_kernel32 = GetModuleHandle(szKernel32);
    GetModuleFileName(h_kernel32, ker_path, 50);

    GetCurrentThreadId_addrs = GetProcAddress(h_kernel32, "GetCurrentThreadId");
    sub_id = GetCurrentThreadId_addrs();
    itoa(sub_id, sub_id_char, 10);

    strncat(ker_path, ": id = ", 10);
    strncat(ker_path, sub_id_char, 10);
    MessageBox(NULL, ker_path, TEXT("Win_prog"), MB_ICONINFORMATION);

    return 0;
}

int main()
{
    int t = 0;
    handle = CreateThread(NULL, 0, ThreadFun, &t, 0, NULL);

    WaitForSingleObject(handle, INFINITE);
}