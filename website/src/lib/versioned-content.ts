export type ContentPlatform = 'android' | 'iphone' | 'common';
export type ContentPurpose = 'setup' | 'verify' | 'remove' | 'uncertain' | 'not_covered' | 'recovery';
export type ContentReleaseStatus = 'current' | 'stale' | 'withdrawn';

export type ContentRelease = {
  status: ContentReleaseStatus;
  sourceCatalogueTask: string;
  sourceCatalogueVersion: string;
  sourceCatalogueBlob: string;
  instructionBindingsBlob: string;
  instructionBindingsSchemaVersion: string;
  sourceArtifact: string;
  sourceCommit: string;
  lastVerified: string;
};

export type BindingsMetadata = {
  schemaVersion: string;
  sourceArtifact: string;
  sourceCommit: string;
  lastVerified: string;
};

const INSTRUCTION_IDS = {
  android: {
    setup: 'INS-AND-SETUP-01',
    verify: 'INS-AND-VERIFY-01',
    remove: 'INS-AND-REMOVE-01',
  },
  iphone: {
    setup: 'INS-IOS-SETUP-01',
    verify: 'INS-IOS-VERIFY-01',
    remove: 'INS-IOS-REMOVE-01',
  },
  common: {
    uncertain: 'INS-COMMON-UNCERTAIN-01',
    not_covered: 'INS-COMMON-NOTCOVERED-01',
    recovery: 'INS-COMMON-RECOVERY-01',
  },
} as const;

export function resolveInstructionId(platform: ContentPlatform, purpose: ContentPurpose): string | null {
  const platformMap = INSTRUCTION_IDS[platform] as Partial<Record<ContentPurpose, string>>;
  return platformMap[purpose] ?? null;
}

export function selectContentRelease(
  releases: Record<string, ContentRelease>,
  releaseId: string,
):
  | { status: 'ready'; releaseId: string; release: ContentRelease }
  | { status: 'stale' | 'withdrawn'; releaseId: string; release: ContentRelease }
  | { status: 'missing_release' | 'invalid_release'; releaseId: string } {
  const release = releases[releaseId];
  if (!release) return { status: 'missing_release', releaseId };
  if (release.status === 'stale' || release.status === 'withdrawn') {
    return { status: release.status, releaseId, release };
  }
  if (release.status !== 'current') return { status: 'invalid_release', releaseId };
  return { status: 'ready', releaseId, release };
}

export function validateBindingsMetadata(release: ContentRelease, metadata: BindingsMetadata): boolean {
  return (
    metadata.schemaVersion === release.instructionBindingsSchemaVersion &&
    metadata.sourceArtifact === release.sourceArtifact &&
    metadata.sourceCommit === release.sourceCommit &&
    metadata.lastVerified === release.lastVerified
  );
}

export function resolveContentDelivery({
  releases,
  releaseId,
  platform,
  purpose,
  availableInstructionIds,
  bindingsMetadata,
}: {
  releases: Record<string, ContentRelease>;
  releaseId: string;
  platform: ContentPlatform;
  purpose: ContentPurpose;
  availableInstructionIds: readonly string[];
  bindingsMetadata: BindingsMetadata;
}) {
  const selected = selectContentRelease(releases, releaseId);
  if (selected.status !== 'ready') return selected;

  const instructionId = resolveInstructionId(platform, purpose);
  if (!instructionId) {
    return { status: 'unsupported' as const, releaseId, release: selected.release };
  }
  if (!validateBindingsMetadata(selected.release, bindingsMetadata)) {
    return { status: 'integrity_error' as const, releaseId, instructionId, release: selected.release };
  }
  if (!availableInstructionIds.includes(instructionId)) {
    return { status: 'missing_instruction' as const, releaseId, instructionId, release: selected.release };
  }
  return { status: 'ready' as const, releaseId, instructionId, release: selected.release };
}
