import { publicRuntimeStatus } from '@/lib/runtime-config';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

export async function GET(): Promise<Response> {
  const status = publicRuntimeStatus();
  return Response.json(status, {
    status: status.ready ? 200 : 503,
    headers: { 'Cache-Control': 'no-store' },
  });
}
