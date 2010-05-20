test_template = """
`timescale $timescale
//`include "testlib.vh"

module auto_test();
  // Setup simulation dumping or not
    initial begin : setup
        $$display("");
        $$display("<%0t> Dump file set to $dumpfile.", $$time);
        $$dumpfile("$dumpfile");
        if ($$test$$plusargs("DUMPON")) begin
            $$display("<%0t> Dumping started.", $$time);
            $$dumpvars(0,tb);
        end
        else
        $$display("<%0t> Dumping has been turned OFF. Nothing will be dumped.", $$time);
        
        $$display("");
        runsim;
//        $$finish;
        `simulation_finish;
    end
    
    task runsim;
    begin
        fork : auto_tests
        begin : auto_tests_run
            $$display("<%0t> Starting Auto Tests", $$time);
            $tasks
            disable auto_tests;
        end
        begin
            #$timeout;   // Timeout
            $$display("<%0t> Timeout.", $$time);
            disable auto_tests_run;
            disable auto_tests;
        end
        join
    end
    endtask
endmodule"""
