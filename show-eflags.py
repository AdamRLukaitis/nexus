#!/usr/bin/python

import sys

FLAGDEFINE = """
#define FL_CF		0x00000001	// Carry Flag
#define FL_UNKNOWN	0x00000002
#define FL_PF		0x00000004	// Parity Flag
#define FL_AF		0x00000010	// Auxiliary carry Flag
#define FL_ZF		0x00000040	// Zero Flag
#define FL_SF		0x00000080	// Sign Flag
#define FL_TF		0x00000100	// Trap Flag
#define FL_IF		0x00000200	// Interrupt Flag
#define FL_DF		0x00000400	// Direction Flag
#define FL_OF		0x00000800	// Overflow Flag
#define FL_IOPL_1	0x00001000	//   IOPL == 1
#define FL_IOPL_2	0x00002000	//   IOPL == 2
#define FL_IOPL_3	0x00003000	//   IOPL == 3
#define FL_NT		0x00004000	// Nested Task
#define FL_RF		0x00010000	// Resume Flag
#define FL_VM		0x00020000	// Virtual 8086 mode
#define FL_AC		0x00040000	// Alignment Check
#define FL_VIF		0x00080000	// Virtual Interrupt Flag
#define FL_VIP		0x00100000	// Virtual Interrupt Pending
#define FL_ID		0x00200000	// ID flag
"""

if len(sys.argv) < 2:
    exit(0)

if sys.argv[1].find('0x') >= 0:
    ef = int(sys.argv[1], 16)
else:
    ef = int(sys.argv[1])
eflags = []

for line in FLAGDEFINE.split('\n'):
    if len(line) < 3: continue
    flag = line.split()[1]
    value = int(line.split()[2], 16)
    eflags.append((value, flag))

eflags.sort(key=lambda e: e[0], reverse=True)
for e in eflags:
    if ef >= e[0]:
        ef -= e[0]
        print e[1]
