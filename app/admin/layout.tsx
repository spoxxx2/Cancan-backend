import { requireAdmin } from "@/lib/admin-check";
import AdminNav from "@/components/AdminNav";

export default async function AdminLayout({ children }) {
  const isAdmin = await requireAdmin();

  if (!isAdmin) {
    return (
      <div className="p-10 text-red-600 text-xl">
        Access denied — admin only.
      </div>
    );
  }

  return (
    <div className="flex min-h-screen">
      <AdminNav />
      <main className="flex-1 p-8 bg-gray-50">{children}</main>
    </div>
  );
}
