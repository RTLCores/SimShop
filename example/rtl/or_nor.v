/*
  Copyright (C) 2011 RTLCores LLC.
  http://rtlcores.com

  Creation Date : 16-Mar-2010
  Support Email : support@rtlcores.com
  Support Forum : http://rtlcores.com/forum

  Descripton
    Simple combinational OR/NOR logic example

  ================================
  Truth Table for 'or' and 'nor'
  ================================
  in1 in0 || or_out | nor_out
  --------||--------|--------
  0   0  ||   0    |    1
  0   1  ||   1    |    0
  1   0  ||   1    |    0
  1   1  ||   1    |    0
*/

`timescale 1 ns / 10 ps

module or_nor (
    input  wire in0,
    input  wire in1,
    output wire or_out,
    output wire nor_out
);

assign or_out = in0 | in1;

assign nor_out = ~(in0 | in1);

endmodule
