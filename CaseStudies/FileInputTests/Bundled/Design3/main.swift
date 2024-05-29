// Bundled

/* 
    I would rather have validation inside the class, since
    validation is 'part of' the class, wheras parsing is more
    'a way of getting' the class
*/
import Foundation

// Class for holding parameters
class Parameters {
    let name: String // Default values not needed now!
    let height: Int
    let weight: Double

    // Very basic initializer now.  We could even use a struct instead 🤔
    init(_ name: String,_ height: Int, _ weight: Double) throws {
        (self.name, self.height, self.weight) = (name, height, weight)
    }

}

func get_input(_ filename: String) throws -> Parameters {

    let lines = try String(contentsOfFile: filename, encoding: String.Encoding.utf8)
        .components(separatedBy: "\n")
    
    let name: String = lines[1]
    if name.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
        throw ParamError("Name must not be blank!")
    }    
    let height: Int = Int(lines[3]) ?? 0
    if height <= 0 {
        throw ParamError("Height must be positive!")
    }
    let weight: Double = Double(lines[5]) ?? 0
    if weight <= 0 {
        throw ParamError("Weight must be positive!")
    }

    return try Parameters(name, height, weight)
}

// Simple error struct
struct ParamError: LocalizedError {
    let description: String

    init(_ description: String) {
        self.description = description
    }

    var errorDescription: String? {
        description
    }
}

var p: Parameters = try get_input("FileInputTests/input.txt")
print("Parameters(\"" + p.name + "\", " + String(p.height) + ", " + String(p.weight) + ")")