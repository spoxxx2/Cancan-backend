import { ReactNode } from "react"
import AdminNav from "@/components/AdminNav"
import { requireAdmin } from "@/lib/admin-check"

export default async function AdminLayout({ children }: { children: ReactNode }) {
  const isAdmin = await requireAdmin()

    // TODO: handle unauthorized access
  }

  return (
    <div>
      <AdminNav />
      {children}
    </div>
  )
}

