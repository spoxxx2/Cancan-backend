import { ReactNode } from "react"
import AdminNav from "@/components/AdminNav"
import { requireAdmin } from "@/lib/admin-check"

export default async function AdminLayout({ children }: { children: ReactNode }) {
  const isAdmin = await requireAdmin()

  if (!isAdmin) {
    return null
  }

  return (
    <div>
      <AdminNav />
      {children}
    </div>
  )
}