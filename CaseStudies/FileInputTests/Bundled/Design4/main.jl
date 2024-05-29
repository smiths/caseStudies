# Bundled

#=
    This is actually super elegant, at least for this size.
    the issue is that it could make the constructor really long if we do it this
    way.  The good news is, Designs 5 and 6 have similar constraints that are
    still modular.
=#

# Struct for holding parameters.
struct Parameters
    name::AbstractString
    height::Integer
    weight::AbstractFloat
end

function Parameters(filename::AbstractString)
    
    # get_input
    file = open(filename, "r")
    lines = readlines(file)
    close(file)

    name = lines[2]
    height = parse(Int32, lines[4])
    weight = parse(Float64, lines[6])

    # input_constraints
    if isempty(strip(name))
        throw("Name must not be blank!")
    elseif height <= 0
        throw("Height must be positive!")
    elseif weight <= 0
        throw("Weight must be positive!")
    end

    return Parameters(name, height, weight)
end

p = Parameters("FileInputTests/input.txt")
println(p)