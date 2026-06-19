module mux2x1(
    input logic a,
    input logic b,
    input logic sel,
    output logic y
);

assign y = sel ? b : a;

endmodule
