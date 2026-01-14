import Link from "next/link";

export default function AdminNav() {
  return (
    <nav className="w-64 bg-white border-r p-6 space-y-4">
      <h1 className="text-2xl font-bold">CANCAN Admin</h1>

      <ul className="space-y-2">
        <li><Link href="/admin">Dashboard</Link></li>
        <li><Link href="/admin/volunteers">Volunteers</Link></li>
        <li><Link href="/admin/cleanups">Cleanups</Link></li>
        <li><Link href="/admin/events">Events</Link></li>
        <li><Link href="/admin/daily-reports">Daily Reports</Link></li>
        <li><Link href="/admin/metrics">Metrics</Link></li>
        <li><Link href="/admin/logs">Logs</Link></li>
        <li><Link href="/admin/system">System</Link></li>
        <li><Link href="/admin/dois">DOIs</Link></li>
      </ul>
    </nav>
  );
}