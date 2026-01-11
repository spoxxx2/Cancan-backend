import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET() {
  try {
    const filePath = path.join(process.cwd(), 'digital_twin_log.json');
    const fileData = fs.readFileSync(filePath, 'utf8');
    return NextResponse.json(JSON.parse(fileData));
  } catch (error) {
    return NextResponse.json({ error: "Metadata log not found" }, { status: 404 });
  }
}
