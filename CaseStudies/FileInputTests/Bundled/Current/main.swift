// Bundled

import Foundation

// Class for holding parameters
class Parameters {
    var name: String = "" // They still need default values, because setting them
    var height: Int = 0   // in another method isn't good enough for Swift
    var weight: Double = 0

    init(_ filename: String) throws {

        try self.get_input(filename)
        try self.input_constraints()
    }

    private func get_input(_ filename: String) throws -> Void {

        let lines = try String(contentsOfFile: filename, encoding: String.Encoding.utf8)
            .components(separatedBy: "\n")
        
        self.name = lines[1]
        self.height = Int(lines[3]) ?? 0
        self.weight = Double(lines[5]) ?? 0
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

var p: Parameters = try Parameters("FileInputTests/input.txt")
print("Parameters(\"" + p.name + "\", " + String(p.height) + ", " + String(p.weight) + ")")