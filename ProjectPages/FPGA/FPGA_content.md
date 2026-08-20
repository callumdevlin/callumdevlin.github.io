---
title: FPGA Notes
permalink: /ProjectPages/FPGA/
description: >
  Working notes on FPGA development — what FPGAs are good for, how the
  toolchain flow works, and reference snippets.
---

This section collects my working notes on FPGA development. These are written as reference notes rather than a project showcase — project write-ups will be added here as they're completed.

## FPGA vs Microcontroller — When and Why

A microcontroller runs instructions one after another on a fixed processor; an FPGA *becomes* the circuit you describe. That distinction drives everything about when each is the right tool:

| | Microcontroller | FPGA |
|:--|:--|:--|
| Execution | Sequential instructions | Massively parallel logic |
| Timing | Software-dependent, jitter from interrupts | Deterministic to the clock edge |
| Strengths | Control logic, comms stacks, low cost, easy tooling | High-speed parallel I/O, custom protocols, DSP pipelines, precise timing |
| Iteration | Flash and run in seconds | Synthesis + place & route, minutes |

The practical rule: if the problem is "do these steps in order, talk to these peripherals", a microcontroller wins on effort and cost. The moment the problem becomes "respond within nanoseconds", "process many channels simultaneously", or "implement a protocol no chip exists for", the FPGA earns its complexity. Plenty of real systems use both — an MCU for housekeeping with an FPGA handling the fast path.

## The Toolchain Flow

FPGA development follows the same pipeline regardless of vendor (Vivado for AMD/Xilinx, Quartus for Intel/Altera, or the open-source Yosys/nextpnr flow for Lattice parts):

1. **Describe** the hardware in an HDL — Verilog/SystemVerilog or VHDL.
2. **Simulate** — verify behaviour with a testbench *before* touching hardware. This is where most real debugging belongs; on-chip debugging is far slower.
3. **Synthesise** — the HDL is converted to a netlist of logic primitives.
4. **Place & route** — the netlist is mapped onto the chip's actual LUTs, flip-flops and routing fabric, checked against your timing constraints.
5. **Generate the bitstream** and program the device.

The constraints file matters as much as the HDL: it tells the tools which physical pins your signals use and what clock speeds the design must meet.

## A Minimal Verilog Example

The "hello world" of FPGA work — an LED blinker — already demonstrates the core ideas of clocked logic and registers:

~~~verilog
module blink (
    input  wire clk,      // e.g. 12 MHz board clock
    output wire led
);
    reg [23:0] counter = 0;

    always @(posedge clk)
        counter <= counter + 1;

    assign led = counter[23];   // MSB toggles at ~0.7 Hz
endmodule
~~~

Two things worth internalising even from this trivial design: nothing here "runs" line by line — the counter increments on *every* clock edge as physical flip-flops, and `assign` is a wire, not an assignment statement. Thinking in hardware rather than software is the entire learning curve.

## Notes Coming Soon

Planned additions to this section: clock domain crossing (the classic source of "it works in sim" bugs), simulation workflow with testbenches and waveform viewers, and project write-ups as they're finished.
