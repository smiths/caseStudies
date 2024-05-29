// Bundled

import Foundation

// Class for holding parameters
class Parameters {
    let name: String // Default values not needed now!
    let height: Int
    let weight: Double

    init(_ name: String,_ height: Int, _ weight: Double) throws {

        (self.name, self.height, self.weight) = (name, height, weight)
        try self.input_constraints()
    }

    private func input_constraints() throws -> Void {

        if self.name.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
            throw ParamError("Name must not be blank!")
        }
        else if self.height <= 0 {
            throw ParamError("Height must be positive!")
        }
        else if self.weight <= 0 {
            throw ParamError("Weight must be positive!")
        }
    }

}

func get_input(_ filename: String) throws -> Parameters {

    let lines = try String(contentsOfFile: filename, encoding: String.Encoding.utf8)
        .components(separatedBy: "\n")
    
    let name: String = lines[1]
    let height: Int = Int(lines[3]) ?? 0
    let weight: Double = Double(lines[5]) ?? 0

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