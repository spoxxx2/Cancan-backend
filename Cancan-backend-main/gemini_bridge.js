const { GoogleGenerativeAI } = require("@google/generative-ai");
const fs = require("fs");

const genAI = new GoogleGenerativeAI("AIzaSyB2KR3LIZ8DeH9JY4MqhouIvqHL1w-0giE");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

async function hardwire(task) {
    const context = fs.readFileSync('./sync_workspace.js', 'utf8');
    const prompt = `Context: ${context}\n\nTask: ${task}`;
    const result = await model.generateContent(prompt);
    console.log(result.response.text());
}

hardwire(process.argv[2] || "Analyze my current setup");
