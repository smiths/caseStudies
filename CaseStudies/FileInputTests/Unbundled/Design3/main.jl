# Unbundled
#=
    I like the key-value pairs, but I miss the type-safety of tuples.
    Also, there's still no help from the compiler for knowing that a key exists.
=#

struct tempParameters
    name::String
    height::Integer
    weight::AbstractFloat
end

function get_input(filename::AbstractString)::tempParameters # Loss of type safety unfortunately
    
    file = open(filename, "r")
    lines = readlines(file)
    close(file)

    name = lines[2]
    height = parse(Int32, lines[4])
    weight = parse(Float64, lines[6])

    return tempParameters(name, height, weight)
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

p = get_input("FileInputTests/input.txt")

# This is a bit clearer of where the values are coming from
(name, height, weight) = (p.name, p.height, p.weight)
input_constraints(name, height, weight)
println(p)