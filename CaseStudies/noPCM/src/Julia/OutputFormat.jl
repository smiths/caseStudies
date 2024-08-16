module OutputFormat

function write_output(E_W::Float64, T_W::Array{Float64})
    outputfile = open("output.txt", "w")
    print(outputfile, "T_W = ")
    println(outputfile, T_W)
    print(outputfile, "E_W = ")
    println(outputfile, E_W)
    close(outputfile)
end

end