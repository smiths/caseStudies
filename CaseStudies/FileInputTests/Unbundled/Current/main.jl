# Unbundled
#=
    This isn't a problem with Julia, but personally I think it's only
    elegant for at most 3 input parameters.  After that you really need
    a better way of saying what's what.
=#

function get_input(filename::AbstractString)::Tuple{String, Int32, Float64}
    
    file = open(filename, "r")
    lines = readlines(file)
    close(file)

    name = lines[2]
    height = parse(Int32, lines[4])
    weight = parse(Float64, lines[6])

    return name, height, weight
end

function input_constraints(name::AbstractString, height::Integer, weight::AbstractFloat)::Nothing

    if isempty(strip(name))
        throw("Name must not be blank!")
    elseif height <= 0
        throw("Height must be positive!")
    elseif weight <= 0
        throw("Weight must be positive!")
    end
end

p = (name, height, weight) = get_input("FileInputTests/input.txt")
input_constraints(name, height, weight)
println(p)