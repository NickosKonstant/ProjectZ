namespace Freecon
{
    using System;
    using System.Data.Entity;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Linq;

    public partial class Freecon : DbContext
    {
        public Freecon()
            : base("name=Freecon")
        {
        }

        public virtual DbSet<Member> Members { get; set; }
        public virtual DbSet<MemberService> MemberServices { get; set; }
        public virtual DbSet<Service> Services { get; set; }
        public virtual DbSet<sysdiagram> sysdiagrams { get; set; }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Member>()
                .HasMany(e => e.MemberServices)
                .WithOptional(e => e.Member)
                .HasForeignKey(e => e.MemberID);
        }
    }
}
